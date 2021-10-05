from django.conf import settings
import stripe
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views import View
from aless_art_shop.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from stripe_payments.email.send_email import confirmation_email, error_email
from aless_art_shop.models import Donation

stripe.api_key = settings.STRIPE_PRIVATE_KEY

if settings.DEBUG == True:
    DOMAIN = 'http://127.0.0.1:8000'
else:
    DOMAIN = 'https://www.artlessi.co.uk'

success_url = DOMAIN + '/stripe_payments/success/'
cancel_url = DOMAIN + '/stripe_payments/cancel/'


class SuccessView(TemplateView):
    template_name = "stripe_payments/success.html"


class CancelView(TemplateView):
    template_name = "stripe_payments/cancel.html"


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        """Creates a session to display the product, as listed in Stripe and redirects to stripe for checkout"""
        product = Product.objects.get(id=self.kwargs["pk"])

        checkout_session = stripe.checkout.Session.create(
            shipping_address_collection={
                'allowed_countries': ['GB'],
            },
            line_items=[
                {
                    'price': product.stripe_price_id,
                    'quantity': 1,
                },
            ],
            payment_method_types=[
                'card',
            ],
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return redirect(checkout_session.url)


# Donations classes

class Donate(TemplateView):
    template_name = "stripe_payments/donate.html"


class MakeDonation(View):
    """To make a fixed amount donation using stripe checkout. Not dynamic"""

    def post(self, request, *args, **kwargs):
        donation_object = Donation.objects.get(amount=self.kwargs["amount"])
        donation_session = stripe.checkout.Session.create(
            line_items=[

                {
                    'price': donation_object.stripe_price_id,
                    'quantity': 1,
                },
            ],
            payment_method_types=[
                'card',
            ],
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url.replace("cancel", "donate"),
        )

        return redirect(donation_session.url, code=303)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except ValueError as e:
        # An invalid payment
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session["customer_details"]["email"]
        delivery_address_object = session["shipping"]["address"]
        customer_name = session["shipping"]["name"]
        if customer_email and delivery_address_object and customer_name:
            # If a purchase was made then all of these fields should exist, send confirmation
            try:
                confirmation_email(customer_name, customer_email, delivery_address_object, False)
            except:
                error_email(customer_name, customer_email, delivery_address_object)
                return None
        elif customer_email:
            # If there was a donation, only the customer_email exists, so send a donation confirmation
            try:
                confirmation_email(None, customer_email, None, True)
            except:
                error_email(False, False, False)
        else:
            # If there was an error then send a minimal email if possible, otherwise notify me
            try:
                confirmation_email(False, customer_email, False, False)
            except:
                error_email(False, False, False)
    return HttpResponse(status=200)
