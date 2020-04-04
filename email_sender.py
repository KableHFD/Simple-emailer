import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = "Blake Merriman"
email['to'] = "blake.a.merriman@gmail.com"
email['subject'] = 'READ!'

email.set_content(html.substitute(name='Blake'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('kable.hfd@gmail.com', 'Blake12471')
	smtp.send_message(email)
	print('all good boss!')