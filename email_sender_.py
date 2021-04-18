import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['From']='Shobhit Singh Pal'
email['TO'] = 'reciever@gmail.com'
email['Subject'] = 'You have won 1,000,000 dollars'

email.set_content(html.substitute({'name':'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
   smtp.ehlo()
   smtp.starttls()
   smtp.login('me@gmail.com','me_pass')
   smtp.send_message(email)
   print('all good boos!') 

