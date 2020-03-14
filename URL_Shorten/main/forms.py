from django import forms
from .models import short_urls


class UrlForm(forms.ModelForm):
    class Meta:
        model = short_urls
        fields = ['long_url']
        widgets = {
            'long_url': forms.TextInput(attrs=({'class': 'url-input'}))
        }
