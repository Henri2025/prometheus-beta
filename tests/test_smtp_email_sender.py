import pytest
from src.smtp_email_sender import send_email

def test_send_email_invalid_inputs():
    """Test handling of invalid input parameters"""
    with pytest.raises(ValueError):
        send_email('', '', '', '', '')  # Empty inputs
    
    with pytest.raises(ValueError):
        send_email(None, None, None, None, None)  # None inputs

def test_send_email_mock_success(mocker):
    """Test successful email sending using mocking"""
    # Mock the SMTP connection and methods
    mock_smtp = mocker.patch('smtplib.SMTP')
    mock_instance = mock_smtp.return_value.__enter__.return_value

    # Simulate successful email sending
    result = send_email(
        sender_email='test@example.com', 
        sender_password='password123', 
        recipient_email='recipient@example.com', 
        subject='Test Subject', 
        body='Test Body'
    )

    # Verify calls and result
    assert result is True
    mock_instance.starttls.assert_called_once()
    mock_instance.login.assert_called_once()
    mock_instance.send_message.assert_called_once()

def test_send_email_smtp_exception(mocker):
    """Test handling of SMTP exceptions"""
    # Mock the SMTP connection to raise an exception
    mock_smtp = mocker.patch('smtplib.SMTP')
    mock_instance = mock_smtp.return_value.__enter__.return_value
    mock_instance.login.side_effect = smtplib.SMTPException("Authentication failed")

    # Test that the function returns False on SMTP exception
    result = send_email(
        sender_email='test@example.com', 
        sender_password='password123', 
        recipient_email='recipient@example.com', 
        subject='Test Subject', 
        body='Test Body'
    )

    assert result is False