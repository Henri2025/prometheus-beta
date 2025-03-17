import os
import pytest
import requests
import tempfile
from src.file_downloader import download_file

@pytest.fixture
def mock_requests(requests_mock):
    return requests_mock

def test_download_file_with_default_save_path(mock_requests):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Mock the response
        mock_content = b'Test file content'
        mock_url = 'https://example.com/testfile.txt'
        mock_requests.get(mock_url, content=mock_content)

        # Change current working directory to temp directory
        original_cwd = os.getcwd()
        os.chdir(tmpdir)

        try:
            # Download the file
            saved_path = download_file(mock_url)

            # Verify file was saved correctly
            assert os.path.exists(saved_path)
            assert os.path.basename(saved_path) == 'testfile.txt'
            
            # Check file contents
            with open(saved_path, 'rb') as f:
                assert f.read() == mock_content
        finally:
            # Restore original working directory
            os.chdir(original_cwd)

def test_download_file_with_custom_save_path(mock_requests):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Construct custom save path
        custom_path = os.path.join(tmpdir, 'downloaded', 'custom_file.txt')

        # Mock the response
        mock_content = b'Custom file content'
        mock_url = 'https://example.com/customfile.txt'
        mock_requests.get(mock_url, content=mock_content)

        # Download the file
        saved_path = download_file(mock_url, custom_path)

        # Verify file was saved correctly
        assert os.path.exists(saved_path)
        assert saved_path == os.path.abspath(custom_path)
        
        # Check file contents
        with open(saved_path, 'rb') as f:
            assert f.read() == mock_content

def test_download_file_invalid_url():
    # Test empty URL
    with pytest.raises(ValueError, match="Invalid URL"):
        download_file('')

    # Test non-string URL
    with pytest.raises(ValueError, match="Invalid URL"):
        download_file(None)

def test_download_file_network_error(mock_requests):
    # Simulate network error
    mock_url = 'https://example.com/nonexistent'
    mock_requests.get(mock_url, status_code=404)

    with pytest.raises(requests.RequestException):
        download_file(mock_url)

def test_download_file_directory_creation(mock_requests):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Construct path in a nested directory that doesn't exist
        custom_path = os.path.join(tmpdir, 'new_dir', 'downloaded_file.txt')

        # Mock the response
        mock_content = b'Directory creation test'
        mock_url = 'https://example.com/testfile.txt'
        mock_requests.get(mock_url, content=mock_content)

        # Download the file
        saved_path = download_file(mock_url, custom_path)

        # Verify file was saved and directory was created
        assert os.path.exists(saved_path)
        assert os.path.dirname(saved_path) == os.path.join(tmpdir, 'new_dir')