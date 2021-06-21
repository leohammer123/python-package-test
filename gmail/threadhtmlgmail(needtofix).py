import smtplib
import os 
from email.message import EmailMessage
import threading
import time

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
<!-- modify this form HTML and place wherever you want your form -->

<form
  action="https://script.google.com/macros/s/AKfycbyejDBdwbbqJLXz_f-i9SFtwdPhiKCbqhshzH25XNeI2FCz3maBrxSAS_kQsrHmmidL/exec"
  method="POST"
>
  <label>
    Your email:
    <input type="email" name="_replyto">
  </label>
  <label>
    Your message:
    <textarea name="message"></textarea>
  </label>

  <!-- your other form fields go here -->

  <button type="submit">Send</button>
</form>
""",subtype = 'html')


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(profile,pw)
    begin = time.perf_counter()
    def send_message():
      smtp.send_message(msg)
    thread = []
    a = threading.Thread(target = send_message)
    for i in range(10):
      thread.append(a)
    for r in range(10):
      thread[r].start()
      print(threading.active_count())
      time.sleep(10)
    end = time.perf_counter()
    print('process finished ____________________________________')
    print(f'it take {end-begin} seconds.')


    smtp.quit()
    #https://formspree.io/f/mayajkvz