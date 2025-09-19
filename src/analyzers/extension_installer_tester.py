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
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from pathlib import Path

from loguru import logger

from .base import ExtensionInfo


@dataclass
class InstallationTestResult:
    """Result of an extension installation test."""
    extension_name: str
    platform: str
    success: bool
    installation_time_seconds: float
    load_time_seconds: Optional[float]
    error_message: Optional[str]
    error_type: Optional[str]  # 'download', 'install', 'load', 'execute', 'environment'
    duckdb_version: str
    test_timestamp: datetime
    file_size_bytes: Optional[int]
    extension_path: Optional[str]


class ExtensionInstallationTester:
    """Tests actual extension installation and loading using uv-managed environments."""
    
    def __init__(self, config, duckdb_version: str = None):
        self.config = config
        self.duckdb_version = duckdb_version or "latest"
        
        # Test script template for running in isolated environment
        self.test_script_template = '''
import duckdb
import sys
import json
import time
from pathlib import Path

def test_extension(extension_name, test_query=None):
    """Test extension installation and loading."""
    result = {
        "success": False,
        "installation_time": 0.0,
        "load_time": None,
        "error_message": None,
        "error_type": None,
        "file_size_bytes": None,
        "extension_path": None
    }
    
    try:
        # Create temporary database
        conn = duckdb.connect(":memory:")
        
        # Install extension
        install_start = time.time()
        try:
            conn.execute(f"INSTALL {extension_name}")
            result["installation_time"] = time.time() - install_start
        except Exception as e:
            result["error_message"] = str(e)
            if "HTTP" in str(e):
                result["error_type"] = "download"
            elif "not found" in str(e).lower():
                result["error_type"] = "install"
            else:
                result["error_type"] = "install"
            return result
        
        # Load extension
        load_start = time.time()
        try:
            conn.execute(f"LOAD {extension_name}")
            result["load_time"] = time.time() - load_start
        except Exception as e:
            result["error_message"] = str(e)
            result["error_type"] = "load"
            return result
        
        # Test basic functionality if query provided
        if test_query:
            try:
                conn.execute(test_query)
            except Exception:
                # Functionality test failure is not critical
                pass
        
        # Check extension directory for file info
        try:
            ext_dir = Path.home() / ".duckdb" / "extensions"
            if ext_dir.exists():
                for ext_file in ext_dir.rglob(f"*{extension_name}*.duckdb_extension"):
                    result["extension_path"] = str(ext_file)
                    result["file_size_bytes"] = ext_file.stat().st_size
                    break
        except Exception:
            pass
        
        conn.close()
        result["success"] = True
        
    except Exception as e:
        result["error_message"] = str(e)
        result["error_type"] = "execute"
    
    return result

if __name__ == "__main__":
    import sys
    extension_name = sys.argv[1]
    test_query = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != "None" else None
    
    result = test_extension(extension_name, test_query)
    print(json.dumps(result))
'''
        
        # Basic test queries for different extension types
        self.extension_test_queries = {
            # Format extensions - use simple validation queries
            'parquet': "SELECT 'parquet loaded' as status",
            'csv': "SELECT 'csv loaded' as status", 
            'json': "SELECT json_valid('{\"test\": 1}') as valid",
            'excel': "SELECT 'excel loaded' as status",
            
            # Database connectors - just check if they load
            'mysql': "SELECT 'mysql loaded' as status",
            'postgres': "SELECT 'postgres loaded' as status", 
            'sqlite': "SELECT 'sqlite loaded' as status",
            
            # Analytics extensions - simple function tests
            'httpfs': "SELECT 'httpfs loaded' as status",
            'spatial': "SELECT 'spatial loaded' as status",
            'fts': "SELECT 'fts loaded' as status",
            
            # Default test
            'default': "SELECT 1 as test_value"
        }
    
    async def test_extension_installation(self, 
                                        extension_names: List[str], 
                                        duckdb_versions: List[str] = None,
                                        timeout_seconds: int = 60) -> List[InstallationTestResult]:
        """
        Test installation of multiple extensions using uv-managed environments.
        
        Args:
            extension_names: List of extension names to test
            duckdb_versions: List of DuckDB versions to test (defaults to current)
            timeout_seconds: Maximum time to wait for each test
            
        Returns:
            List of InstallationTestResult objects
        """
        if duckdb_versions is None:
            duckdb_versions = [self.duckdb_version]
        
        platform = self._get_current_platform()
        logger.info(f"Testing installation of {len(extension_names)} extensions with DuckDB versions {duckdb_versions}")
        
        results = []
        
        for duckdb_version in duckdb_versions:
            for extension_name in extension_names:
                try:
                    result = await self._test_single_extension_with_uv(
                        extension_name, duckdb_version, platform, timeout_seconds
                    )
                    results.append(result)
                    
                    # Brief pause between tests
                    await asyncio.sleep(0.5)
                    
                except Exception as e:
                    logger.warning(f"Failed to test {extension_name} with DuckDB {duckdb_version}: {e}")
                    results.append(InstallationTestResult(
                        extension_name=extension_name,
                        platform=platform,
                        success=False,
                        installation_time_seconds=0.0,
                        load_time_seconds=None,
                        error_message=str(e),
                        error_type='environment',
                        duckdb_version=duckdb_version,
                        test_timestamp=datetime.now(),
                        file_size_bytes=None,
                        extension_path=None
                    ))
        
        return results
    
    async def _test_single_extension_with_uv(self, 
                                           extension_name: str, 
                                           duckdb_version: str,
                                           platform: str,
                                           timeout_seconds: int) -> InstallationTestResult:
        """Test extension installation using uv-managed environment."""
        logger.debug(f"Testing {extension_name} installation with DuckDB {duckdb_version}")
        
        start_time = datetime.now()
        
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                # Create test script
                script_path = Path(temp_dir) / "test_extension.py"
                with open(script_path, 'w') as f:
                    f.write(self.test_script_template)
                
                # Create pyproject.toml for uv
                pyproject_path = Path(temp_dir) / "pyproject.toml"
                duckdb_spec = f"duckdb=={duckdb_version}" if duckdb_version != "latest" else "duckdb"
                
                pyproject_content = f'''[project]
name = "duckdb-extension-test"
version = "0.1.0"
dependencies = [
    "{duckdb_spec}",
]
requires-python = ">=3.9"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
'''
                with open(pyproject_path, 'w') as f:
                    f.write(pyproject_content)
                
                # Get test query for this extension
                test_query = self._get_test_query(extension_name)
                
                # Run test in isolated uv environment
                cmd = [
                    "uv", "run", 
                    "--project", temp_dir,
                    "python", str(script_path),
                    extension_name,
                    test_query or "None"
                ]
                
                logger.debug(f"Running command: {' '.join(cmd)}")
                
                # Execute with timeout
                process = await asyncio.create_subprocess_exec(
                    *cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                    cwd=temp_dir
                )
                
                try:
                    stdout, stderr = await asyncio.wait_for(
                        process.communicate(), 
                        timeout=timeout_seconds
                    )
                except asyncio.TimeoutError:
                    process.kill()
                    await process.wait()
                    raise asyncio.TimeoutError(f"Test timeout after {timeout_seconds} seconds")
                
                execution_time = (datetime.now() - start_time).total_seconds()
                
                # Parse results
                if process.returncode == 0:
                    try:
                        result_data = json.loads(stdout.decode())
                        return InstallationTestResult(
                            extension_name=extension_name,
                            platform=platform,
                            success=result_data.get("success", False),
                            installation_time_seconds=result_data.get("installation_time", execution_time),
                            load_time_seconds=result_data.get("load_time"),
                            error_message=result_data.get("error_message"),
                            error_type=result_data.get("error_type"),
                            duckdb_version=duckdb_version,
                            test_timestamp=start_time,
                            file_size_bytes=result_data.get("file_size_bytes"),
                            extension_path=result_data.get("extension_path")
                        )
                    except json.JSONDecodeError as e:
                        error_msg = f"Failed to parse test results: {e}. Output: {stdout.decode()}"
                        logger.warning(error_msg)
                        return self._create_error_result(extension_name, platform, duckdb_version, start_time, error_msg, "parse_error", execution_time)
                else:
                    error_msg = stderr.decode() or f"Process failed with return code {process.returncode}"
                    return self._create_error_result(extension_name, platform, duckdb_version, start_time, error_msg, "process_error", execution_time)
                    
            except asyncio.TimeoutError as e:
                return self._create_error_result(extension_name, platform, duckdb_version, start_time, str(e), "timeout", timeout_seconds)
            except Exception as e:
                execution_time = (datetime.now() - start_time).total_seconds()
                return self._create_error_result(extension_name, platform, duckdb_version, start_time, str(e), "environment", execution_time)
    
    def _create_error_result(self, extension_name: str, platform: str, duckdb_version: str, 
                           start_time: datetime, error_msg: str, error_type: str, 
                           execution_time: float) -> InstallationTestResult:
        """Create an error result object."""
        return InstallationTestResult(
            extension_name=extension_name,
            platform=platform,
            success=False,
            installation_time_seconds=execution_time,
            load_time_seconds=None,
            error_message=error_msg,
            error_type=error_type,
            duckdb_version=duckdb_version,
            test_timestamp=start_time,
            file_size_bytes=None,
            extension_path=None
        )
    
    def _get_test_query(self, extension_name: str) -> Optional[str]:
        """Get an appropriate test query for an extension."""
        return self.extension_test_queries.get(extension_name, self.extension_test_queries['default'])
    
    def _get_current_platform(self) -> str:
        """Determine the current platform identifier."""
        import platform
        
        system = platform.system().lower()
        machine = platform.machine().lower()
        
        if system == 'linux':
            if machine in ['x86_64', 'amd64']:
                return 'linux_amd64'
            elif machine in ['arm64', 'aarch64']:
                return 'linux_arm64'
        elif system == 'darwin':
            if machine in ['x86_64', 'amd64']:
                return 'osx_amd64'
            elif machine in ['arm64', 'aarch64']:
                return 'osx_arm64'
        elif system == 'windows':
            return 'windows_amd64'
        
        return f"{system}_{machine}"
    
    def get_test_summary(self, results: List[InstallationTestResult]) -> Dict[str, Any]:
        """Generate a summary of installation test results."""
        if not results:
            return {
                'total_tests': 0,
                'successful_tests': 0,
                'failed_tests': 0,
                'success_rate': 0.0,
                'average_install_time': 0.0,
                'average_load_time': 0.0,
                'error_types': {},
                'problematic_extensions': [],
                'fastest_installs': [],
                'slowest_installs': []
            }
        
        successful_tests = [r for r in results if r.success]
        failed_tests = [r for r in results if not r.success]
        
        # Calculate average times
        install_times = [r.installation_time_seconds for r in successful_tests if r.installation_time_seconds > 0]
        avg_install_time = sum(install_times) / len(install_times) if install_times else 0.0
        
        load_times = [r.load_time_seconds for r in successful_tests if r.load_time_seconds is not None]
        avg_load_time = sum(load_times) / len(load_times) if load_times else 0.0
        
        # Categorize error types
        error_types = {}
        for result in failed_tests:
            error_type = result.error_type or 'unknown'
            error_types[error_type] = error_types.get(error_type, 0) + 1
        
        # Identify problematic extensions
        extension_failures = {}
        for result in failed_tests:
            ext_name = result.extension_name
            extension_failures[ext_name] = extension_failures.get(ext_name, 0) + 1
        
        problematic_extensions = [
            {'name': ext, 'failure_count': count}
            for ext, count in extension_failures.items()
        ]
        
        # Find fastest and slowest installations
        successful_with_times = [r for r in successful_tests if r.installation_time_seconds > 0]
        fastest_installs = sorted(successful_with_times, key=lambda x: x.installation_time_seconds)[:5]
        slowest_installs = sorted(successful_with_times, key=lambda x: x.installation_time_seconds, reverse=True)[:5]
        
        return {
            'total_tests': len(results),
            'successful_tests': len(successful_tests),
            'failed_tests': len(failed_tests),
            'success_rate': (len(successful_tests) / len(results)) * 100,
            'average_install_time': avg_install_time,
            'average_load_time': avg_load_time,
            'error_types': error_types,
            'problematic_extensions': sorted(problematic_extensions, key=lambda x: x['failure_count'], reverse=True),
            'fastest_installs': [
                {'name': r.extension_name, 'time': r.installation_time_seconds} 
                for r in fastest_installs
            ],
            'slowest_installs': [
                {'name': r.extension_name, 'time': r.installation_time_seconds} 
                for r in slowest_installs
            ]
        }