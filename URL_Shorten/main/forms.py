from django import forms
from .models import short_urls
from django.utils.translation import ugettext_lazy as _


class UrlForm(forms.ModelForm):

    # short_url = forms.CharField(required=False, label='Token')

    class Meta:
        model = short_urls
        fields = ('short_url', 'long_url')
        labels = {
            'short_url': _('Token'),
        }
        widgets = {
            'long_url': forms.TextInput(attrs=({'class': 'url-input'})),
            'short_url': forms.TextInput(attrs=({'class': 'url-input'}))
        }

    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.fields['short_url'].required = False
