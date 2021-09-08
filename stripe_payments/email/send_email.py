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

smtp_server = "smtpout.secureserver.net"
sender_email = "alessio@artlessi.co.uk"

def confirmation_email(receiver):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Thanks for your order!"
    message["From"] = sender_email
    message["To"] = receiver

    plain_text = """
        Thank you so much for your purchase!
        Your order is being processed
        
        Your order has been received and is being processed.
        
        In the meantime, feel free to email me at alessartshop@gmail.com if you have any questions or check out the 
        faqs page here. """

    html_text = """
    <html>
      <body>
      <h1>Thank you so much for your purchase! </h1>
        <p>Your order is being processed
        </p>
        <p>Your order has been received and is being processed.</p>
        <p>In the meantime, feel free to email me at 
            <a href="mailto:alessio@artlessi.co.uk">alessio@artlessi.co.uk</a>
         if you have any questions or check out the <a href = "{% url 'stripe_payments:#' %}"> faqs <a/> page here.<p/>
      </body>
    </html>
    """
    #todo add an image to the email

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
