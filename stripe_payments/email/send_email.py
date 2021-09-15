import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from dotenv import load_dotenv
import os
import base64

load_dotenv()

port = 465  # For SSL

password = os.getenv('GMAIL')

# Create a secure SSL context
context = ssl.create_default_context()

smtp_server = "smtpout.secureserver.net"
sender_email = "alessio@artlessi.co.uk"


def confirmation_email(receiver):
    message = MIMEMultipart("related")
    message["Subject"] = "Thanks for your order!"
    message["From"] = sender_email
    message["To"] = receiver

    encoded = base64.b64encode(open(r"C:\Users\Alessio\programming\Python\art_shop\static\am_logo.png", 'rb').read()).decode()

    plain_text = """
        Thank you so much for your purchase!
       
        Your order has been received and is being processed.
        
        In the meantime, feel free to email me at alessartshop@gmail.com if you have any questions or check out the 
        faqs page. """

    html_text = f"""
    <html>
      <body>
        <img src="data:image/png;base64,{encoded}" width="120" height="150">
        <h1>Thank you so much for your purchase! </h1>
        <p>I'm so pleased you like my art and have decided to buy something!</p>
        <p>Your order has been received and is being processed.</p>
        <p>The item will be shipped as soon as possible and you will receive a shipping confirmation</p>
        <p>In the meantime, feel free to email me at 
            <a href="mailto:alessio@artlessi.co.uk">alessio@artlessi.co.uk</a>
         if you have any questions or check out the page <a href = "https://www.artlessi.co.uk"> faqs <a/> here.<p/>
        <p>Lots of love, Alessi</p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    # part1 = MIMEText(plain_text, 'plain')
    part2 = MIMEText(html_text, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    # message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver, message.as_string())
    return "email sent"


if __name__ == "__main__":
    confirmation_email("alessio@artlessi.co.uk")
