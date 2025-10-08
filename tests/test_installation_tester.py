"""
Tests for InstallationTester class and its special case handling.

These tests verify that the InstallationTester correctly handles both normal
extension installation testing and special cases like jemalloc.
"""

import asyncio
import platform
import pytest
from unittest.mock import Mock, patch, AsyncMock
from pathlib import Path

from src.analyzers.installation_tester import InstallationTester, InstallationTestResult


class TestInstallationTester:
    """Test suite for InstallationTester class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.tester = InstallationTester()

    def test_init(self):
        """Test InstallationTester initialization."""
        assert self.tester is not None
        assert hasattr(self.tester, 'platform')
        assert hasattr(self.tester, 'test_script_template')

    def test_get_current_platform_macos_arm64(self):
        """Test platform detection for macOS ARM64."""
        with patch('platform.system', return_value='Darwin'):
            with patch('platform.machine', return_value='arm64'):
                tester = InstallationTester()
                assert tester.platform == 'osx_arm64'

    def test_get_current_platform_macos_amd64(self):
        """Test platform detection for macOS AMD64."""
        with patch('platform.system', return_value='Darwin'):
            with patch('platform.machine', return_value='x86_64'):
                tester = InstallationTester()
                assert tester.platform == 'osx_amd64'

    def test_get_current_platform_linux(self):
        """Test platform detection for Linux."""
        with patch('platform.system', return_value='Linux'):
            with patch('platform.machine', return_value='x86_64'):
                tester = InstallationTester()
                assert tester.platform == 'linux_amd64'

    def test_get_current_platform_windows(self):
        """Test platform detection for Windows."""
        with patch('platform.system', return_value='Windows'):
            with patch('platform.machine', return_value='AMD64'):
                tester = InstallationTester()
                assert tester.platform == 'windows_amd64'


class TestSpecialCaseHandling:
    """Test special case handling for problematic extensions."""

    def setup_method(self):
        """Set up test fixtures."""
        self.tester = InstallationTester()

    def test_jemalloc_special_case_macos(self):
        """Test jemalloc special case handling on macOS."""
        with patch.object(self.tester, '_get_current_platform', return_value='osx_arm64'):
            with patch('platform.python_version', return_value='3.13.0'):
                result = self.tester._handle_special_cases('jemalloc')
                
                assert result is not None
                assert isinstance(result, InstallationTestResult)
                assert result.extension_name == 'jemalloc'
                assert result.success is False
                assert result.install_time is None
                assert result.load_time is None
                assert result.total_time == 0.0
                assert 'statically linked' in result.error_message
                assert 'osx_arm64' in result.error_message
                assert result.python_version == '3.13.0'
                assert result.duckdb_version_used == 'N/A'
                assert result.test_environment == 'special_case'

    def test_jemalloc_special_case_windows(self):
        """Test jemalloc special case handling on Windows."""
        with patch.object(self.tester, '_get_current_platform', return_value='windows_amd64'):
            with patch('platform.python_version', return_value='3.13.0'):
                result = self.tester._handle_special_cases('jemalloc')
                
                assert result is not None
                assert result.success is False
                assert 'statically linked' in result.error_message
                assert 'windows_amd64' in result.error_message

    def test_jemalloc_special_case_linux(self):
        """Test jemalloc special case handling on Linux."""
        with patch.object(self.tester, '_get_current_platform', return_value='linux_amd64'):
            with patch('platform.python_version', return_value='3.13.0'):
                result = self.tester._handle_special_cases('jemalloc')
                
                assert result is not None
                assert result.success is False
                assert 'statically linked' in result.error_message
                assert 'cannot be installed or loaded at runtime' in result.error_message
                assert 'built into DuckDB' in result.error_message

    def test_non_special_case_extension(self):
        """Test that normal extensions don't trigger special case handling."""
        result = self.tester._handle_special_cases('json')
        assert result is None

        result = self.tester._handle_special_cases('parquet')
        assert result is None

        result = self.tester._handle_special_cases('httpfs')
        assert result is None

    def test_unknown_extension(self):
        """Test that unknown extensions don't trigger special case handling."""
        result = self.tester._handle_special_cases('unknown_extension')
        assert result is None


class TestExtensionTesting:
    """Test extension installation testing functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.tester = InstallationTester()

    @pytest.mark.asyncio
    async def test_test_extensions_batch_with_special_case(self):
        """Test batch testing that includes special case extensions."""
        extension_names = ['json', 'jemalloc', 'parquet']
        
        # Mock the normal extension testing
        mock_result_json = InstallationTestResult(
            extension_name='json',
            success=True,
            install_time=0.1,
            load_time=0.05,
            functional_test_time=0.02,
            total_time=0.15,
            error_message=None,
            python_version='3.13',
            duckdb_version_used='1.1.3',
            test_environment='uv'
        )
        
        mock_result_parquet = InstallationTestResult(
            extension_name='parquet',
            success=True,
            install_time=0.2,
            load_time=0.08,
            functional_test_time=0.03,
            total_time=0.28,
            error_message=None,
            python_version='3.13',
            duckdb_version_used='1.1.3',
            test_environment='uv'
        )

        # Mock the single extension testing method
        async def mock_test_single(ext_name):
            if ext_name == 'json':
                return mock_result_json
            elif ext_name == 'parquet':
                return mock_result_parquet
            else:
                raise ValueError(f"Unexpected extension: {ext_name}")

        with patch.object(self.tester, '_test_single_extension_with_uv', side_effect=mock_test_single):
            with patch.object(self.tester, '_get_current_platform', return_value='osx_arm64'):
                with patch('platform.python_version', return_value='3.13.0'):
                    with patch('asyncio.sleep', return_value=None):  # Skip sleep in tests
                        results = await self.tester.test_extensions_batch(extension_names)

        assert len(results) == 3
        
        # Check that jemalloc was handled as special case
        jemalloc_result = next(r for r in results if r.extension_name == 'jemalloc')
        assert jemalloc_result.success is False
        assert jemalloc_result.test_environment == 'special_case'
        assert 'statically linked' in jemalloc_result.error_message
        
        # Check that normal extensions were processed normally
        json_result = next(r for r in results if r.extension_name == 'json')
        assert json_result.success is True
        assert json_result.test_environment == 'uv'
        
        parquet_result = next(r for r in results if r.extension_name == 'parquet')
        assert parquet_result.success is True
        assert parquet_result.test_environment == 'uv'

    @pytest.mark.asyncio
    async def test_test_extensions_batch_with_exception(self):
        """Test batch testing handles exceptions gracefully."""
        extension_names = ['failing_extension']
        
        # Mock an exception during testing
        with patch.object(
            self.tester, 
            '_test_single_extension_with_uv', 
            side_effect=Exception("Test error")
        ):
            with patch('platform.python_version', return_value='3.13.0'):
                results = await self.tester.test_extensions_batch(extension_names)

        assert len(results) == 1
        result = results[0]
        assert result.extension_name == 'failing_extension'
        assert result.success is False
        assert result.error_message == 'Test error'
        assert result.python_version == '3.13.0'

    @pytest.mark.asyncio
    async def test_test_single_extension_timeout(self):
        """Test that single extension testing handles timeouts properly."""
        extension_name = 'slow_extension'
        
        # Create a mock process that times out
        mock_process = Mock()
        mock_process.communicate = AsyncMock()
        mock_process.communicate.side_effect = asyncio.TimeoutError()
        mock_process.kill = Mock()
        mock_process.wait = AsyncMock()
        
        with patch('asyncio.create_subprocess_exec', return_value=mock_process):
            with patch('tempfile.TemporaryDirectory'):
                with patch('pathlib.Path.write_text'):
                    result = await self.tester._test_single_extension_with_uv(extension_name)
        
        assert result.extension_name == extension_name
        assert result.success is False
        assert "timed out" in result.error_message
        mock_process.kill.assert_called_once()

    @pytest.mark.asyncio
    async def test_test_single_extension_success(self):
        """Test successful single extension testing."""
        extension_name = 'test_extension'
        
        # Mock successful process execution
        mock_stdout = '{"success": true, "install_time": 0.1, "load_time": 0.05, "total_time": 0.15, "error_message": null, "python_version": "3.13", "duckdb_version_used": "1.1.3", "test_environment": "uv"}'
        
        mock_process = Mock()
        mock_process.communicate = AsyncMock(return_value=(mock_stdout.encode(), b''))
        mock_process.returncode = 0
        
        with patch('asyncio.create_subprocess_exec', return_value=mock_process):
            with patch('tempfile.TemporaryDirectory'):
                with patch('pathlib.Path.write_text'):
                    result = await self.tester._test_single_extension_with_uv(extension_name)
        
        assert result.extension_name == extension_name
        assert result.success is True
        assert result.install_time == 0.1
        assert result.load_time == 0.05
        assert result.total_time == 0.15
        assert result.python_version == "3.13"
        assert result.duckdb_version_used == "1.1.3"

    @pytest.mark.asyncio
    async def test_test_single_extension_process_failure(self):
        """Test single extension testing with process failure."""
        extension_name = 'failing_extension'
        
        # Mock failed process execution
        mock_process = Mock()
        mock_process.communicate = AsyncMock(return_value=(b'', b'Process failed with error'))
        mock_process.returncode = 1
        
        with patch('asyncio.create_subprocess_exec', return_value=mock_process):
            with patch('tempfile.TemporaryDirectory'):
                with patch('pathlib.Path.write_text'):
                    result = await self.tester._test_single_extension_with_uv(extension_name)
        
        assert result.extension_name == extension_name
        assert result.success is False
        assert "Process failed with error" in result.error_message

    def test_test_script_template_content(self):
        """Test that the test script template contains required components."""
        template = self.tester.test_script_template
        
        # Check for essential imports
        assert 'import duckdb' in template
        assert 'import json' in template
        assert 'import time' in template
        
        # Check for main test function
        assert 'def test_extension(extension_name, test_query=None):' in template
        
        # Check for DuckDB operations
        assert 'duckdb.connect(' in template
        assert 'INSTALL' in template
        assert 'LOAD' in template
        
        # Check for result structure
        assert '"success"' in template
        assert '"install_time"' in template
        assert '"load_time"' in template
        assert '"error_message"' in template


class TestInstallationTestResult:
    """Test InstallationTestResult dataclass."""

    def test_installation_test_result_creation(self):
        """Test creating InstallationTestResult instances."""
        result = InstallationTestResult(
            extension_name='test_ext',
            success=True,
            install_time=0.1,
            load_time=0.05,
            functional_test_time=0.02,
            total_time=0.15,
            error_message=None,
            python_version='3.13',
            duckdb_version_used='1.1.3',
            test_environment='uv'
        )
        
        assert result.extension_name == 'test_ext'
        assert result.success is True
        assert result.install_time == 0.1
        assert result.load_time == 0.05
        assert result.total_time == 0.15
        assert result.error_message is None
        assert result.python_version == '3.13'
        assert result.duckdb_version_used == '1.1.3'
        assert result.test_environment == 'uv'

    def test_installation_test_result_failure(self):
        """Test creating failure InstallationTestResult instances."""
        result = InstallationTestResult(
            extension_name='failing_ext',
            success=False,
            install_time=None,
            load_time=None,
            functional_test_time=None,
            total_time=0.0,
            error_message='Extension failed to install',
            python_version='3.13',
            duckdb_version_used='unknown',
            test_environment='uv'
        )
        
        assert result.extension_name == 'failing_ext'
        assert result.success is False
        assert result.install_time is None
        assert result.load_time is None
        assert result.total_time == 0.0
        assert result.error_message == 'Extension failed to install'