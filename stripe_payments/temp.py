from stripe_payments.email.send_email import confirmation_email, error_email
import json

with open(r'C:\Users\Alessio\programming\Python\tests.txt') as json_file:
    ob = json.load(json_file)

if ob['object']:
    session = ob["object"]
    customer_email = session["customer_details"]["email"]
    try:
        delivery_address_object = session["shipping"]["address"]
        customer_name = session["shipping"]["name"]
        if customer_email and delivery_address_object and customer_name:
            try:
                confirmation_email(customer_name, customer_email, delivery_address_object, False)
                print("confirmed")
            except:
                error_email()
                print("errored")

    except:

            # If a purchase was made then all of these fields should exist, send confirmation
            try:
                confirmation_email(False, customer_email, False, True)
                print("confirmed donation")

            except:
                error_email()
                print("error")

