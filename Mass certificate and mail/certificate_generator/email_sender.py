import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, message, attachments=None):
    try:
        # Create a multipart message
        email = MIMEMultipart()
        email['From'] = sender_email
        email['To'] = receiver_email
        email['Subject'] = subject

        # Add the message body
        email.attach(MIMEText(message, 'plain'))

        # Add attachments, if any
        if attachments:
            for attachment in attachments:
                with open(attachment, 'rb') as file:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{attachment}"')
                email.attach(part)

        # Connect to the SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(sender_email, sender_password)

        # Send the email
        smtp_connection.send_message(email)
        smtp_connection.quit()

        print(f"Email sent to {receiver_email}")

    except smtplib.SMTPException as e:
        print(f"Failed to send email to {receiver_email}: {str(e)}")
