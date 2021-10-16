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

message = MIMEMultipart("related")
message["From"] = f"Artlessi <{sender_email}>"
logo_file_path = str(Path(__file__).parents[2] / "static" / "am_logo.png")
encoded = base64.b64encode(open(logo_file_path, 'rb').read()).decode()


def smtp_send(receiver):
    """Function to perform the last action of sending email"""
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver, message.as_string())


def confirmation_email(customer_name, receiver, delivery_address_object, donation=False):
    """ A success email sent to customer"""
    if donation:
        message["Subject"] = "Thanks for your donation!"
        email_text = f"""
        <html>
          <body>
            <img src="data:image/jpg;base64,{encoded}" width="120" height="150">
            <h1>Thank you so much for your Donation! </h1>
            <p>Hi!, I'm so pleased you like my art and have decided to contribute!</p>
            <p>This means so much to me and I will continue to make art thanks to your donation</p>
            <p>Feel free to email me at
                <a href="mailto:alessio@artlessi.co.uk">alessio@artlessi.co.uk</a>
             if you have any questions or want to buy/commission some work!<p/>
            <p>Lots of love, Alessio</p>
          </body>
        </html>
        """
    elif not customer_name and not delivery_address_object:
        email_text = f"""
        <html>
          <body>
            <img src="data:image/jpg;base64,{encoded}" width="120" height="150">
            <h1>Thank you so much for your purchase! </h1>
            <p>Hi! I'm so pleased you like my art and have decided to buy something!</p>
            <p>Your order has been received and is being processed.</p>
            <p>The item will be shipped as soon as possible and you will receive a shipping confirmation</p>
            <p>In the meantime, feel free to email me at
                <a href="mailto:alessio@artlessi.co.uk">alessio@artlessi.co.uk</a>
             if you have any questions or check out the faqs page <a href = "https://www.artlessi.co.uk">here.<a/><p/>
            <p>Lots of love, Alessio</p>
          </body>
        </html>
        """
    else:
        address_fields, address_array = ["city", "country", "line1", "line2", "postal_code"], []
        for field in address_fields:
            if delivery_address_object[field]:
                address_array.append(delivery_address_object[field])

        delivery_address = " ".join(address_array)
        email_text = f"""
        <html>
          <body>
            <img src="data:image/jpg;base64,{encoded}" width="120" height="150">
            <h1>Thank you so much for your purchase! </h1>
            <p>Hi {customer_name}, I'm so pleased you like my art and have decided to buy something!</p>
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

        message["Subject"] = "Thanks for your order!"

    message["To"] = receiver

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(email_text, "html")
    message.attach(part1)

    smtp_send(receiver)
    return "confirmation email sent"


def error_email(customer_name, customer_email, delivery_address_object):
    """ An error email sent to myself to flag that the confirmation email failed"""
    if not customer_name and not customer_email and not delivery_address_object:
        error_message = f"""The email notification did not work for the latest purchase. The fields entered to the name, email and address were not valid. Check the logs"""
    else:
        error_message = f"""The email notification did not work for the latest purchase. Customer: {customer_name}, email: {customer_email}, address: {delivery_address_object}"""
    message["Subject"] = "Email confirmation error"
    message["To"] = sender_email

    part1 = MIMEText(error_message, "html")
    message.attach(part1)
    smtp_send(sender_email)

    return "error email sent"


if __name__ == "__main__":
    error_email(None, None,None)
