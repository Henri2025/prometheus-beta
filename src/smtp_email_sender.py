import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email: str, 
               sender_password: str, 
               recipient_email: str, 
               subject: str, 
               body: str, 
               smtp_server: str = 'smtp.gmail.com', 
               smtp_port: int = 587) -> bool:
    """
    Send an email using SMTP protocol.

    Args:
        sender_email (str): Email address of the sender
        sender_password (str): Password for the sender's email account
        recipient_email (str): Email address of the recipient
        subject (str): Subject line of the email
        body (str): Body text of the email
        smtp_server (str, optional): SMTP server address. Defaults to Gmail's SMTP server.
        smtp_port (int, optional): SMTP server port. Defaults to 587 (TLS).

    Returns:
        bool: True if email sent successfully, False otherwise

    Raises:
        ValueError: If any required parameters are missing or invalid
    """
    # Validate input parameters
    if not all([sender_email, sender_password, recipient_email, subject, body]):
        raise ValueError("All email parameters must be non-empty")

    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Establish a secure session with the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable TLS encryption
            server.login(sender_email, sender_password)
            
            # Send the email
            server.send_message(message)

        return True

    except smtplib.SMTPException as e:
        # Log or handle SMTP-specific exceptions
        print(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return False