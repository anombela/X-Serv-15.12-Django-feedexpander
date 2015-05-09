from django.shortcuts import render
from models import Persona, Tweet
from django.http import HttpResponse
import feedparser
from django.core.exceptions import ObjectDoesNotExist
import urllib


# Create your views here.

def mifeed(request, username):
    url = "https://twitrss.me/twitter_user_to_rss/?user=" + username
    dicc = feedparser.parse(url)
    salida = ""

    for number in range(5):
        salida += dicc.entries[number].title + "<br>"
        urls = dicc.entries[number].title.split()
        for url in urls:
            if url.startswith("http://") or url.startswith("https://"):
                url = url.split('&')[0]
                salida += "<li><a href=" + url + ">" + url + "</a></li>"
                soup = BeautifulSoup(urllib.urlopen(url).read())
                salida += str(soup.p).decode('utf8')
                salida += str(soup.img).decode('utf8') + "<br><br>"

        user = dicc.entries[number].title.split(':')[0]
        try:
            t = User.objects.get(name=user)
        except ObjectDoesNotExist:
            t = User(name=user)
            t.save()

        try:
            t = Tweet.objects.get(content=dicc.entries[number].title)
        except ObjectDoesNotExist:
            t = Tweet(content=dicc.entries[number].title,
                      url=dicc.entries[number].link, name=t)
            t.save()

    return HttpResponse(salida)
