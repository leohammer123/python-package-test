import smtplib
import os 

pw = os.environ.get('mypw')

print(pw)


with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()

