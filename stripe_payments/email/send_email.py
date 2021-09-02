import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

port = 465   # For SSL
password = os.getenv('GMAIL')
# Create a secure SSL context
context = ssl.create_default_context()

smtp_server = "smtp.gmail.com"
sender_email = "alessartshop@gmail.com"
receiver_email = "your@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Thanks for your order!"
message["From"] = sender_email
message["To"] = sender_email

plain_text = """
Hi Aless
"""

html_text = """
<html>
  <body>
    <p><a href = "www.google.com">Hi, How are you?<a/>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(plain_text, "plain")
part2 = MIMEText(html_text, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, sender_email, message.as_string())
