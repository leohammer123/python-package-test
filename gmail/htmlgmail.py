import smtplib
import os 
from email.message import EmailMessage
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
<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>test: learn-to-send-email-via-google-script-html-no-server</title>

  <meta name="description" content="Test all HTML form and input elements for learn-to-send-email-via-google-script-html-no-server." />
  <meta name="author" content="dwyl">

  <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="style.css">
</head>

<body>

  <h1>Test All Form and Input Elements</h1>
  <p>
    Here is a form that is meant to include all form and input elements possible
    on a page. This way we can test out if the form functions as expected. We
    will populate with default values if possible or using Javascript to
    simplify testing.
  </p>


  <form class="gform pure-form pure-form-stacked" method="POST" data-email="example@email.net" action="https://script.google.com/macros/s/AKfycbyejDBdwbbqJLXz_f-i9SFtwdPhiKCbqhshzH25XNeI2FCz3maBrxSAS_kQsrHmmidL/exec">

    <div class="form-elements">

      <!--submit/button-->
      <button class="button-success pure-button button-xlarge">
        <i class="fa fa-paper-plane"></i>&nbsp;Send
      </button>

      <!--text-field-->
      <fieldset class="pure-group">
        <label for="text">Name: </label>
        <input id="text" name="text" value="What your Mom calls you" />
      </fieldset>

      <!--text-area-->
      <fieldset class="pure-group">
        <label for="text-area">Message: </label>
        <textarea id="text-area" name="text-area" rows="10">Tell us what's on your mind...</textarea>
      </fieldset>

      <!--email-->
      <fieldset class="pure-group">
        <label for="email"><em>Your</em> Email Address:</label>
        <input id="email" name="email" type="email" required value="your.name@email.com" />
      </fieldset>

      <!--color-->
      <fieldset class="pure-group">
        <label for="color">Favourite Color: </label>
        <input id="color" type="color" name="color" />
      </fieldset>

      <!--radio button-->
      <fieldset class="pure-group">
        <label for="radio">Choose a Programming Language: </label>
        <input id="radio" type="radio" name="radio" value="js" checked />Javascript
      </fieldset>

      <!--radio group-->
      <fieldset class="pure-group">
        <legend>OK, Now Really Choose:</legend>
        <input id="radio-group--javascript" type="radio" name="radio-group" value="js" /> <label for="radio-group--javascript">Javascript</label>
        <input id="radio-group--java" type="radio" name="radio-group" value="java" /> <label for="radio-group--java">Java</label>
        <input id="radio-group--cplusplus" type="radio" name="radio-group" value="c++" /> <label for="radio-group--cplusplus">C++</label>
        <input id="radio-group--python" type="radio" name="radio-group" value="python" checked /> <label for="radio-group--python">Python</label>
        <input id="radio-group--other" type="radio" name="radio-group" value="other" /> <label for="radio-group--other">Other</label>
      </fieldset>

      <!--checkbox-->
      <fieldset class="pure-group">
        <label for="checkbox">What are you Most Comfortable With?</label>
        <input id="checkbox" type="checkbox" name="checkbox" value="js" checked />Javascript
      </fieldset>

      <!--checkboxes-->
      <fieldset class="pure-group">
        <legend>What are you Most Comfortable With?</legend>
        <input id="checkboxes--javascript" type="checkbox" name="checkboxes" value="js" checked /> <label for="checkboxes--javascript">Javascript</label>
        <input id="checkboxes--java" type="checkbox" name="checkboxes" value="java" /> <label for="checkboxes--java">Java</label>
        <input id="checkboxes--cplusplus" type="checkbox" name="checkboxes" value="c++" /> <label for="checkboxes--cplusplus">C++</label>
        <input id="checkboxes--python" type="checkbox" name="checkboxes" value="python" checked /> <label for="checkboxes--python">Python</label>
        <input id="checkboxes--other" type="checkbox" name="checkboxes" value="other" checked /> <label for="checkboxes--other">Other</label>
      </fieldset>

      <!--menu-->
      <fieldset class="pure-group">
        <label for="menu">Try Again:</label>
        <select id="menu" name="menu">
          <option selected>Javascript</option>
          <option>Java</option>
          <option>C++</option>
          <option>Python</option>
          <option>Other</option>
        </select>
      </fieldset>

      <!--list-->
      <fieldset class="pure-group">
        <label for="list">And Again:</label>
        <select id="list" name="list" multiple size="5">
          <option selected>Javascript</option>
          <option>Java</option>
          <option>C++</option>
          <option selected>Python</option>
          <option>Other</option>
        </select>
      </fieldset>

      <!--datalist-->
      <fieldset class="pure-group">
        <label for="datalist">And Yet Again!:</label>
        <input id="datalist" list="progLang" name="datalist" value="C++" />
        <datalist id="progLang">
          <option value="Javascript" />
          <option value="Java" />
          <option value="C++" />
          <option value="Python" />
          <option value="Other" />
        </datalist>
      </fieldset>

      <!--date-->
      <fieldset class="pure-group">
        <label for="date">Date</label>
        <input id="date" type="date" name="date" value="2017-03-16" />
      </fieldset>

      <!--datetime-local-->
      <fieldset class="pure-group">
        <label for="datetime-local">Datetime local</label>
        <input id="datetime-local" type="datetime-local" name="datetime-local" value="2017-03-16T23:59:59" />
      </fieldset>

      <!--month-->
      <fieldset class="pure-group">
        <label for="month">Month</label>
        <input id="month" type="month" name="month" value="2017-10" />
      </fieldset>

      <!--number-->
      <fieldset class="pure-group">
        <label for="number">Number</label>
        <input id="number" type="number" name="number" value="3" />
      </fieldset>

      <!--range-->
      <fieldset class="pure-group">
        <label for="range">Range</label>
        <input id="range" type="range" name="range" value="76" min="0" max="100" />
      </fieldset>

      <!--search-->
      <fieldset class="pure-group">
        <label for="search">Search</label>
        <input id="search" type="search" name="search" value="Bing || Google || DuckDuckGo" />
      </fieldset>

      <!--tel-->
      <fieldset class="pure-group">
        <label for="tel">Tel</label>
        <input id="tel" type="tel" name="tel" value="012-345-6789" />
      </fieldset>

      <!--time-->
      <fieldset class="pure-group">
        <label for="time">Time</label>
        <input id="time" type="time" name="time" value="10:51:36" />
      </fieldset>

      <!--url-->
      <fieldset class="pure-group">
        <label for="url">URL</label>
        <input id="url" type="url" name="url" value="https://github.com/dwyl/learn-to-send-email-via-google-script-html-no-server" />
      </fieldset>

      <!--week-->
      <fieldset class="pure-group">
        <label for="week">Week</label>
        <input id="week" type="week" name="week" value="2017-W51" />
      </fieldset>

      <!--hidden-->
      <input type="hidden" name="hidden" value="this is hidden" />
    </div>

    <div class="thankyou_message" style="display:none;">
      <h2><em>Thanks</em> for contacting us!
        We will get back to you soon!</h2>
    </div>

  </form>

  <!-- showing multiple forms working -->
  <hr style="margin: 50px">

  <form class="gform pure-form pure-form-stacked" method="POST" data-email="example@email.net"
  action="https://script.google.com/macros/s/AKfycbwMxYDrufp73bKdU8gMvxFDdHRuzcR4IKQUB33B7GqwyfyZS04/exec">
    <!-- change the form action to your script url -->

    <div class="form-elements">
      <fieldset class="pure-group">
        <label for="name">Name: </label>
        <input id="name" name="name" placeholder="What your Mom calls you" />
      </fieldset>

      <fieldset class="pure-group">
        <label for="message">Message: </label>
        <textarea id="message" name="message" rows="10"
        placeholder="Tell us what's on your mind..."></textarea>
      </fieldset>

      <fieldset class="pure-group">
        <label for="email"><em>Your</em> Email Address:</label>
        <input id="email" name="email" type="email" value=""
        required placeholder="your.name@email.com"/>
      </fieldset>

      <fieldset class="pure-group">
        <label for="color">Favourite Color: </label>
        <input id="color" name="color" placeholder="green" />
      </fieldset>

      <button class="button-success pure-button button-xlarge">
        <i class="fa fa-paper-plane"></i>&nbsp;Send</button>
    </div>

    <!-- Customise the Thankyou Message People See when they submit the form: -->
    <div class="thankyou_message" style="display:none;">
      <h2><em>Thanks</em> for contacting us again!
        We will get back to you soon!</h2>
    </div>

  </form>

  <script data-cfasync="false" src="form-submission-handler.js"></script>

</body>
</html>
  

""",subtype = 'html')


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(profile,pw)
    begin = time.perf_counter()
    smtp.send_message(msg)
    end = time.perf_counter()
    print('process finished ____________________________________')
    print(f'it take {end-begin} seconds.')


    smtp.quit()
    #https://formspree.io/f/mayajkvz