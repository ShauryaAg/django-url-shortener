from django import forms
from .models import short_urls


class UrlForm(forms.ModelForm):

    short_url = forms.CharField(required=False)

    class Meta:
        model = short_urls
        fields = ['short_url', 'long_url']
        widgets = {
            'short_url': forms.TextInput(attrs=({'class': 'url-input'})),
            'long_url': forms.TextInput(attrs=({'class': 'url-input'}))
        }
