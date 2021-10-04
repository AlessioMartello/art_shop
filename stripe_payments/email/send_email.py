import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import base64
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()

port = 465  # For SSL

password = os.getenv('GMAIL')

# Create a secure SSL context
context = ssl.create_default_context()

smtp_server = "smtpout.secureserver.net"
sender_email = "alessio@artlessi.co.uk"


def confirmation_email(customer_name, receiver, delivery_address_object):

    address_fields, address_array = ["city", "country", "line1", "line2", "postal_code"], []
    for field in address_fields:
        if delivery_address_object[field]:
            address_array.append(delivery_address_object[field])

    delivery_address = " ".join(address_array)

    message = MIMEMultipart("related")
    message["Subject"] = "Thanks for your order!"
    message["From"] = f"Artlessi <{sender_email}>"
    message["To"] = receiver

    logo_file_path = str(Path(__file__).parents[2] / "static" / "am_logo.png")

    encoded = base64.b64encode(open(logo_file_path, 'rb').read()).decode()

    plain_text = """
        Thank you so much for your purchase!

        Your order has been received and is being processed.

        In the meantime, feel free to email me at alessartshop@gmail.com if you have any questions or check out the
        faqs page. """

    html_text = f"""
    <html>
      <body>
        <img src="data:image/png;base64,{encoded}" width="120" height="150">
        <h1>Hi {customer_name}, thank you so much for your purchase! </h1>
        <p>I'm so pleased you like my art and have decided to buy something!</p>
        <p>Your order has been received and is being processed.</p>
        <p>The item will be shipped as soon as possible and you will receive a shipping confirmation</p>
        <p>Delivery address:<br><br><b>{delivery_address}</b></p>
        <p>In the meantime, feel free to email me at
            <a href="mailto:alessio@artlessi.co.uk">alessio@artlessi.co.uk</a>
         if you have any questions or check out the faqs page <a href = "https://www.artlessi.co.uk">here.<a/><p/>
        <p>Lots of love, Alessio</p>
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
    return "confirmation email sent"


def error_email(customer_name, customer_email, delivery_address_object):
    error_message = f""" The email notification did not work for the latest purchase. Customer: {customer_name}, email: {customer_email}, address: {delivery_address_object} """

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, sender_email, error_message.as_string())
    return "error email sent"


if __name__ == "__main__":
    confirmation_email("test name", "alessio@artlessi.co.uk", "Test address")
