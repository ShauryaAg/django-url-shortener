from django.shortcuts import render, redirect
from .models import short_urls
from .forms import UrlForm
from .shortener import shortener


def Make(request):
    form = UrlForm(request.POST)
    a = ""

    url_list = short_urls.objects.all()

    if request.method == "POST":
        if form.is_valid():
            newUrl = form.save(commit=False)
            a = shortener().issue_token()
            newUrl.short_url = a
            newUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"

    return render(request, 'home.html', {'form': form, 'url_list': url_list, 'a': a})


def Home(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)
