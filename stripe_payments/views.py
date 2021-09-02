from django.conf import settings
import stripe
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from aless_art_shop.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


stripe.api_key = settings.STRIPE_PRIVATE_KEY


class ProductListView(ListView):
    model = Product
    template_name = "aless_art_shop/product_list.html"
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = "aless_art_shop/product_detail.html"
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context

class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        """Creates a session to display the product, as listed in Stripe and redirects to stripe for checkout"""
        product = Product.objects.get(id=self.kwargs["pk"])

        DOMAIN = 'http://127.0.0.1:8000'  # todo change me when deployed

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': product.stripe_price_id,
                    'quantity': 1,
                },
            ],
            payment_method_types=[
                'card',
                # 'bacs_debit',
            ],
            mode='payment',
            success_url=DOMAIN + '/success/',
            cancel_url=DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)


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
        payment_intent = session["payment_intent"]

        # todo send email confirmation
    return HttpResponse(status=200)
