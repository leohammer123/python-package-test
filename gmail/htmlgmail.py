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
msg.add_alternative(""" \
    <!doctype html>
<html>
<h1>hello </h1>
<form >
<input type = 'text'/>
<input type = 'submit' value = 'submit' />
</form>

</html>

""",subtype = 'html')


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(profile,pw)
    smtp.send_message(msg)
    smtp.quit()