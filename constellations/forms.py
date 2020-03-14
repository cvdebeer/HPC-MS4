from django.forms import ModelForm
from .models import MailingList


class MailingListForm(ModelForm):
    # full_name = forms.CharField(max_length=100, label='Full Name')
    # email_address = forms.EmailField(label='Your Email Address')
    # accept_tc = forms.BooleanField(label='Accept Terms and Conditions')

    class Meta:
        model = MailingList
        fields = ['full_name', 'email_address', 'Accept terms and conditions']
