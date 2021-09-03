import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

port = 465  # For SSL
password = os.getenv('GMAIL')

# Create a secure SSL context
context = ssl.create_default_context()

smtp_server = "smtp.gmail.com"
sender_email = "alessartshop@gmail.com"

def confirmation_email(receiver):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Thanks for your order!"
    message["From"] = sender_email
    message["To"] = receiver

    # todo make this a more visually appealling email wiith more info, including the product and image etc

    plain_text = """
    Thank you! Your order has been received
    Your order is being processed
    
    In the meantime, feel free to email me at alessartshop@gmail.com if you have any questions.
    """

    html_text = """
    <html>
      <body>
      <h1>Thank you! Your order has been received <h1/>
        <p>Your order is being processed
        </p>
        <p>In the meantime, feel free to email me at alessartshop@gmail.com if you have any questions.
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
        server.sendmail(sender_email, receiver, message.as_string())
    return "email sent"
