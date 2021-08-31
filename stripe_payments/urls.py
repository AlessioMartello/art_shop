# payments/urls.py

from django.urls import path
from stripe_payments.views import CreateCheckoutSessionView, ProductLandingPageView, CancelView, SuccessView, stripe_webhook

from . import views
app_name = "stripe_payments"

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('', ProductLandingPageView.as_view(), name='landing-page'),
]