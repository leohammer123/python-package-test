import smtplib
import os 
import imghdr
from email.message import EmailMessage

pw = 'usxm yfta nnbd lndi'
profile = os.environ.get('PROFILE')
reciver = input ('enter reciver addr\n')



msg = EmailMessage()
msg['Subject'] = input('enter Subject \n')
msg['From'] = profile
msg['To'] = reciver
content = input('plz input ur content\n')
msg.set_content(content)
files = ['test.pdf']


for file in files: #open the file in files
    with open(file,'rb') as f:
        file_data = f.read()
        file_name = f.name #check property
    msg.add_attachment(file_data,maintype = 'application',subtype= 'octet-stream',filename = file_name)


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(profile,pw)
    smtp.send_message(msg)
    smtp.quit()