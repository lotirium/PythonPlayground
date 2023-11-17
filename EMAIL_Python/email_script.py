import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Name'
email['to'] = 'reciever_email@gmail.com'
email['subject'] ='You won 1000000 dollars!'

email.set_content(html.substitute({'name': 'Nia'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email@gmail.com', 'your_password')
    smtp.send_message(email)
    print('all good boss!')
