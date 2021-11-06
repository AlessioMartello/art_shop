
from django.http import HttpResponseRedirect
from django.shortcuts import render
from subscribers.forms import SubscriberForm
from .models import Subscriber

def subscribe(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscriberForm(request.POST or None)
        # check whether it's valid:
        if form.is_valid():
            model = Subscriber()
            model.email = form.cleaned_data['SubscriberEmail']
            model.save()            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            #return render(request, './subscribers/SubscribeForm.html', {'form': form})
            return HttpResponseRedirect('/') # todo Make a thanks page
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubscriberForm()
    return render(request, 'subscribers/SubscribeForm.html', {'form': form})