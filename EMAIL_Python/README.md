# Email Sender Script

This project contains a Python script (`email_script.py`) for sending HTML emails using SMTP, along with an HTML template (`index.html`) for the email content.

## Features

- Sends HTML emails using Python's `smtplib`.
- Uses a template (`index.html`) for the email body.
- Substitutes a placeholder in the HTML template with a dynamic value.

## How to Use

1. Update `your_email@gmail.com` and `your_password` in `email_script.py` with your email and app-specific password.
2. Modify the recipient's email in `email['to']`.
3. Adjust the `index.html` template as needed.
4. Run `email_script.py` to send the email.

## Requirements

- Python 3
- Access to an SMTP server (configured for Gmail by default)

## Important Note

This script is for educational purposes. Ensure you have permission to send emails to the recipients and handle email credentials securely.
