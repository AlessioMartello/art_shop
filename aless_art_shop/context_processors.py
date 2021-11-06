from subscribers.models import Subscriber
from subscribers.forms import SubscriberForm

def add_variable_to_context(request):
    context={}
    context['email'] = Subscriber.objects.all()
    context['form'] = SubscriberForm
    return context