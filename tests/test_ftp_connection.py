import pytest
import ftplib
from src.ftp_connection import establish_ftp_connection

class MockFTP:
    def __init__(self, host=None, timeout=None):
        self.host = host
        self.connected = False
        self.logged_in = False

    def connect(self, host, port):
        self.connected = True
        return "220 MockFTP Server Ready"

    def login(self, user, passwd):
        self.logged_in = True
        return "230 User logged in"

def test_successful_connection(monkeypatch):
    # Mock the FTP class to simulate a successful connection
    monkeypatch.setattr(ftplib, 'FTP', MockFTP)
    
    connection, error = establish_ftp_connection(
        host='test.example.com', 
        username='testuser', 
        password='testpass'
    )
    
    assert connection is not None
    assert error is None

def test_missing_parameters():
    # Test with missing parameters
    connection, error = establish_ftp_connection(
        host='', 
        username='', 
        password=''
    )
    
    assert connection is None
    assert "Missing required connection parameters" in error

def test_invalid_connection_parameters(monkeypatch):
    # Test connection failure
    class MockFailedFTP:
        def __init__(self, timeout=None):
            pass
        def connect(self, host, port):
            raise ftplib.error_perm("Invalid connection parameters")
    
    monkeypatch.setattr(ftplib, 'FTP', MockFailedFTP)
        
    connection, error = establish_ftp_connection(
        host='invalid.host', 
        username='baduser', 
        password='badpass'
    )
        
    assert connection is None
    assert "FTP Connection Error" in error

def test_connection_timeout(monkeypatch):
    # Simulate a timeout scenario
    class MockTimeoutFTP:
        def __init__(self, timeout=None):
            pass
        def connect(self, host, port):
            raise TimeoutError("Connection timed out")
    
    monkeypatch.setattr(ftplib, 'FTP', MockTimeoutFTP)
        
    connection, error = establish_ftp_connection(
        host='slow.example.com', 
        username='timeoutuser', 
        password='timeoutpass'
    )
        
    assert connection is None
    assert "Unexpected Error" in error