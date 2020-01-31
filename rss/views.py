from django.shortcuts import render
from django.http import HttpResponse
from rss.models import Cnn
import feedparser
import sqlite3

# Create your views here.
def cnn_list(request):
    return render(request,'rss/cnn_list.html',{})


def readfeed(request):
    if request.GET.get("url"):
        url = request.GET["url"] #Getting URL
        feed = feedparser.parse(url) #Parsing XML data
        for item in feed["entries"]:
            a = str(item["description"])[:str(item["description"]).find("<img src=")]
            if('Corona' in str(item["title"])):
                q = Cnn(title=item["title"],time=item["published"],content=a,link=item["link"])
                q.save()
            print(len(feed["entries"]))   
            print(str(item["link"]))
            print("-------------------------------")
            print(a)
    else:
         feed = None                  
    return render(request, 'rss/feedreader.html', {'feed' : feed,})     

def showcnn(request):
    listcnn = Cnn.objects.all()
    return render(request,'rss/cnnlist.html',{'listcnn' : listcnn})