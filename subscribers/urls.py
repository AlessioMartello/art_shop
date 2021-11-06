"""Defines URL patterns for aless_art_shop app"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from subscribers.views import successfulSubscriptionView, subscribe

app_name = "subscribers"


urlpatterns = [
    path('', subscribe, name='subscribe'),
    path('SuccessfulSubscription/', successfulSubscriptionView.as_view(), name='subscribe-success'),
]