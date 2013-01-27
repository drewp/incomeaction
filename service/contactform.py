#!/usr/bin/python

import bottle, cgi, traceback, simplemail

def message(fields):
    return """\
Submission from contact form at http://incomeaction.org/

Name: %(name)s
Email: %(email)s
Telephone: %(telephone)s
Message: %(message)s
""" % fields
    
@bottle.route("/")
def index():
    return 'contact form processor for incomeaction. POST to <a href="contact">/contact</a>'

@bottle.route("/contact", method="POST")
def contact():
    try:
        name = bottle.request.forms.name
        msg = message(bottle.request.forms)

        simplemail.Simplemail().send(recipient=['contact@incomeaction.org'],
                                     sender='web form <contact@incomeaction.org>',
                                     subject="incomeaction web form submission from %r" % name,
                                     body=msg)

        thanks = "Thanks for the message, %s!" % cgi.escape(name)
    except Exception:
        traceback.print_exc()
        bottle.response.status = 500
        return "Sorry, we couldn't send that message"
        
    return """\
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Message sent</title>   
  </head>
  <body>
    <p>%s</p>
    <a href="/">Return to site</a>
  </body>
</html>
    """ % thanks

bottle.run(port=9003)
