"""
Real-time Extension Installation Tester for DuckDB Extensions Analysis.

This module uses `uv` to create isolated testing environments and actually
attempts to install and load extensions in DuckDB to verify they work correctly.
"""

import asyncio
import tempfile
import subprocess
import os
import json
import platform
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from pathlib import Path

from loguru import logger


@dataclass
class InstallationTestResult:
    """Result of an extension installation test."""
    extension_name: str
    success: bool
    install_time: Optional[float]
    load_time: Optional[float]
    total_time: float
    error_message: Optional[str]
    python_version: str
    duckdb_version_used: str
    test_environment: str


class InstallationTester:
    """Tests actual extension installation and loading using uv-managed environments."""
    
    def __init__(self):
        self.platform = self._get_current_platform()
        
        # Test script template for running in isolated environment
        self.test_script_template = '''
import duckdb
import sys
import json
import time

def test_extension(extension_name):
    """Test extension installation and loading."""
    result = {
        "success": False,
        "install_time": 0.0,
        "load_time": None,
        "total_time": 0.0,
        "error_message": None,
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}",
        "duckdb_version_used": duckdb.__version__,
        "test_environment": "uv"
    }
    
    total_start = time.time()
    
    try:
        # Create temporary database
        conn = duckdb.connect(":memory:")
        
        # Install extension
        install_start = time.time()
        try:
            conn.execute(f"INSTALL {extension_name}")
            result["install_time"] = time.time() - install_start
        except Exception as e:
            result["error_message"] = str(e)
            result["total_time"] = time.time() - total_start
            return result
        
        # Load extension
        load_start = time.time()
        try:
            conn.execute(f"LOAD {extension_name}")
            result["load_time"] = time.time() - load_start
        except Exception as e:
            result["error_message"] = str(e)
            result["total_time"] = time.time() - total_start
            return result
        
        conn.close()
        result["success"] = True
        
    except Exception as e:
        result["error_message"] = str(e)
    
    result["total_time"] = time.time() - total_start
    return result

if __name__ == "__main__":
    import sys
    extension_name = sys.argv[1]
    
    result = test_extension(extension_name)
    print(json.dumps(result))
'''
    
    def _get_current_platform(self) -> str:
        """Get the current platform identifier."""
        system = platform.system().lower()
        machine = platform.machine().lower()
        
        if system == "darwin":
            if machine == "arm64":
                return "osx_arm64"
            else:
                return "osx_amd64"
        elif system == "linux":
            return "linux_amd64"
        elif system == "windows":
            return "windows_amd64"
        else:
            return f"{system}_{machine}"
    
    def _handle_special_cases(self, extension_name: str) -> Optional[InstallationTestResult]:
        """Handle special case extensions that cannot be tested normally."""
        current_platform = self._get_current_platform()
        
        if extension_name == "jemalloc":
            # jemalloc is statically linked and cannot be installed at runtime
            # It's only available on Linux by default, not on macOS or Windows
            if current_platform.startswith("osx") or current_platform.startswith("windows"):
                return InstallationTestResult(
                    extension_name=extension_name,
                    success=False,
                    install_time=None,
                    load_time=None,
                    total_time=0.0,
                    error_message=f"jemalloc extension is statically linked and not available on {current_platform}. See: https://duckdb.org/docs/stable/core_extensions/jemalloc.html",
                    python_version=f"{platform.python_version()}",
                    duckdb_version_used="N/A",
                    test_environment="special_case"
                )
            else:
                # On Linux, jemalloc is available but still cannot be installed at runtime
                return InstallationTestResult(
                    extension_name=extension_name,
                    success=False,
                    install_time=None,
                    load_time=None,
                    total_time=0.0,
                    error_message="jemalloc extension is statically linked and cannot be installed or loaded at runtime. It's built into DuckDB on this platform.",
                    python_version=f"{platform.python_version()}",
                    duckdb_version_used="N/A",
                    test_environment="special_case"
                )
        
        # Add more special cases here as needed
        # elif extension_name == "another_special_extension":
        #     return InstallationTestResult(...)
        
        return None
    
    async def test_extensions_batch(self, extension_names: List[str]) -> List[InstallationTestResult]:
        """
        Test installation of multiple extensions using uv-managed environments.
        
        Args:
            extension_names: List of extension names to test
            
        Returns:
            List of InstallationTestResult objects
        """
        logger.info(f"Testing installation of {len(extension_names)} extensions")
        
        results = []
        
        for extension_name in extension_names:
            # Handle special cases
            special_case_result = self._handle_special_cases(extension_name)
            if special_case_result:
                results.append(special_case_result)
                continue
                
            try:
                result = await self._test_single_extension_with_uv(extension_name)
                results.append(result)
                
                # Brief pause between tests
                await asyncio.sleep(1)
                
            except Exception as e:
                logger.warning(f"Failed to test {extension_name}: {e}")
                results.append(InstallationTestResult(
                    extension_name=extension_name,
                    success=False,
                    install_time=None,
                    load_time=None,
                    total_time=0.0,
                    error_message=str(e),
                    python_version=f"{platform.python_version()}",
                    duckdb_version_used="unknown",
                    test_environment="uv"
                ))
        
        return results
    
    async def _test_single_extension_with_uv(self, extension_name: str) -> InstallationTestResult:
        """Test a single extension using uv-managed environment."""
        
        # Create temporary directory for this test
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Create pyproject.toml for uv
            pyproject_content = '''[project]
name = "duckdb-extension-test"
version = "0.1.0"
dependencies = ["duckdb>=1.0.0"]

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
'''
            
            (temp_path / "pyproject.toml").write_text(pyproject_content)
            
            # Create test script
            test_script_path = temp_path / "test_extension.py"
            test_script_path.write_text(self.test_script_template)
            
            try:
                # Run the test in uv environment
                cmd = [
                    "uv", "run", "--directory", str(temp_path), 
                    "python", "test_extension.py", extension_name
                ]
                
                process = await asyncio.create_subprocess_exec(
                    *cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                    cwd=temp_path
                )
                
                try:
                    stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=120)
                    
                    if process.returncode == 0:
                        # Parse JSON result
                        result_data = json.loads(stdout.decode())
                        return InstallationTestResult(
                            extension_name=extension_name,
                            success=result_data.get("success", False),
                            install_time=result_data.get("install_time"),
                            load_time=result_data.get("load_time"),
                            total_time=result_data.get("total_time", 0.0),
                            error_message=result_data.get("error_message"),
                            python_version=result_data.get("python_version", "unknown"),
                            duckdb_version_used=result_data.get("duckdb_version_used", "unknown"),
                            test_environment=result_data.get("test_environment", "uv")
                        )
                    else:
                        error_msg = stderr.decode() if stderr else "Process failed"
                        logger.warning(f"Extension test failed for {extension_name}: {error_msg}")
                        
                        return InstallationTestResult(
                            extension_name=extension_name,
                            success=False,
                            install_time=None,
                            load_time=None,
                            total_time=0.0,
                            error_message=error_msg,
                            python_version="unknown",
                            duckdb_version_used="unknown",
                            test_environment="uv"
                        )
                        
                except asyncio.TimeoutError:
                    process.kill()
                    await process.wait()
                    logger.warning(f"Extension test timed out for {extension_name}")
                    
                    return InstallationTestResult(
                        extension_name=extension_name,
                        success=False,
                        install_time=None,
                        load_time=None,
                        total_time=0.0,
                        error_message="Test timed out after 120 seconds",
                        python_version="unknown",
                        duckdb_version_used="unknown",
                        test_environment="uv"
                    )
                    
            except Exception as e:
                logger.error(f"Failed to create uv environment for {extension_name}: {e}")
                return InstallationTestResult(
                    extension_name=extension_name,
                    success=False,
                    install_time=None,
                    load_time=None,
                    total_time=0.0,
                    error_message=f"Environment setup failed: {str(e)}",
                    python_version="unknown",
                    duckdb_version_used="unknown",
                    test_environment="uv"
                )


# Simple test when run directly
if __name__ == "__main__":
    async def test_main():
        tester = InstallationTester()
        results = await tester.test_extensions_batch(["json", "parquet"])
        
        for result in results:
            print(f"\n{result.extension_name}:")
            print(f"  Success: {result.success}")
            print(f"  Install Time: {result.install_time}s")
            print(f"  Load Time: {result.load_time}s") 
            print(f"  Total Time: {result.total_time}s")
            if result.error_message:
                print(f"  Error: {result.error_message}")
    
    asyncio.run(test_main())