from django import forms

from .models import MailingList


class MailingListForm(forms.ModelForm):
    accept_tc = forms.BooleanField(label='Accept Terms and Conditions')

    class Meta:
        model = MailingList
        fields = ['full_name', 'email_address', 'accept_tc']
