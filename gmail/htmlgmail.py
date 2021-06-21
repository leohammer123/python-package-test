import smtplib
import os 
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
<h1>hello There is a small pull </h1>
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname"><br>
  <input type="radio" id="male" name="gender" value="male">
  <label for="male">Male</label><br>
  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label><br>
  <input type="radio" id="other" name="gender" value="other">
  <label for="other">Other</label><br>
  <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
  <label for="vehicle1"> I have a bike</label><br>
  <input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
  <label for="vehicle2"> I have a car</label><br>
  <input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
  <label for="vehicle3"> I have a boat</label><br>
  <input type="submit" value="Submit">
  <p>&#128512;</p>
  <p>&#128512;</p>
<p>&#128512;</p>
  <p>&#128512;</p>
  <p>&#128512;</p>
  <p>&#128512;</p>
  <p>&#128512;</p>
  <p>&#128512;</p>
  <p>&#128512;</p>
</form>

</html>

""",subtype = 'html')


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(profile,pw)
    smtp.send_message(msg)
    smtp.quit()