from excel_reader import read_names_and_emails_from_excel
from certificate_generator_helper import generate_certificate
from email_sender import send_email

def main():
    template_path = "C:/Users/rupes/OneDrive/Desktop/certificate and mail/template.jpg"
    excel_file_path = "C:/Users/rupes/OneDrive/Desktop/certificate and mail/participants1.xlsx"
    output_directory = "C:/Users/rupes/OneDrive/Desktop/certificate and mail/all_printed_certificates"
    sender_email = "rupeshkumarchetri222@gmail.com"  # Your Gmail address
    sender_password = "kxzqaasxmtmkgirf"  # Your Gmail password or app password

    candidates = read_names_and_emails_from_excel(excel_file_path)

    for candidate in candidates:
        candidate_name, receiver_email = candidate

        # Generate certificate
        generate_certificate(candidate_name, template_path, output_directory)

        # Send email with certificate attachment
        subject = "Certificate of Completion"
        message = f"Dear {candidate_name},\n\nCongratulations! Here is your certificate of completion.he he project khatam"

        certificate_path = f"{output_directory}/{candidate_name}_certificate.png"
        attachments = [certificate_path]

        send_email(sender_email, sender_password, receiver_email, subject, message, attachments)

if __name__ == '__main__':
    main()
