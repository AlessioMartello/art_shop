from django import forms


class SubscriberForm(forms.Form):
    SubscriberEmail = forms.EmailField(label='', max_length=100, widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email',
                                   'class':'SubscriberEmailClassCSS'}))
