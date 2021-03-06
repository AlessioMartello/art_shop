from django.urls import path
from stripe_payments.views import CreateCheckoutSessionView, CancelView, SuccessView, stripe_webhook, Donate, MakeDonation, MakeMonthlyDonation
from django.views.decorators.csrf import csrf_exempt

app_name = "stripe_payments"

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('stripe/webhook/', csrf_exempt(stripe_webhook), name='stripe-webhook'),
    path('donate/', Donate.as_view(), name='donate'),
    path('donate/make-donation/<amount>/', MakeDonation.as_view(), name='make-donation'),
    path('donate/make-monthly-donation/<amount>/', MakeMonthlyDonation.as_view(), name='make-monthly-donation'),
]

