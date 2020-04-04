import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = "Insert Name"
email['to'] = "Insert Email"
email['subject'] = 'READ!'

email.set_content(html.substitute(name='name'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('example@gmail.com', 'Password123')
	smtp.send_message(email)
	print('all good boss!')
