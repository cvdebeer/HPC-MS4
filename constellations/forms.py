from django.forms import ModelForm
from .models import MailingList


class MailingListForm(ModelForm):
    class Meta:
        model = MailingList
        fields = ['full_name', 'email_address', 'Accept terms and conditions']
