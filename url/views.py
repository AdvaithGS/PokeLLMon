from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import UrlData
from .forms import Url
import requests
import random
import string
import hashlib

def index(request):
    return HttpResponse("Hello World")

def urlShort(request):
    data = []
    request_data = []
    if request.method == 'POST':
        form = Url(request.POST)
        
        if form.is_valid():
            url = form.cleaned_data["url"]

            
            print(requests.get(int(not url.startswith("https://"))*"https://" + url).status_code)

            if(requests.get(int(not url.startswith("https://"))*"https://" + url).status_code != 200):
                print("INCORRECT!")
                return render(request, 'index.html', {'form': form,'data': [],"request_data" : [], "error" : "Incorrect URL Specified"})
            
            
            #print(type(form.cleaned_data['use_alias'])) #Bool
            #print(form.cleaned_data['custom_slug'])

            if(form.cleaned_data['use_alias']):
                slug = "u/" + form.cleaned_data['custom_slug']
                for entry in UrlData.objects.all():
                    if(entry.slug == slug):
                        return render(request, 'index.html', {'form': form,'data': [],"request_data" : [], "error": "The written slug is already being used by another URL"})
            else:   
                hashed = hashlib.sha256(url.encode()).hexdigest()[:13]
                slug = "u/" + hashed
            
            flag = 0
            for entry in UrlData.objects.all():
                if(entry.slug == slug):
                    flag = 1
            if(not flag):    
                
                new_url = UrlData(url=url, slug=slug)
                new_url.save()
            
            request_data = [UrlData.objects.get(slug=slug)]
            #print(request_data)
            
            context = {
                'form': form,
                'data': data,
                "request_data" : request_data 
            }

            #print(context)
            return render(request, 'index.html', context)
    else:
        form = Url()

    context = {
        'form': form,
        'data': data,
        "request_data" : request_data,
        "error" : ""
    }
    #print(context)
    return render(request, 'index.html', context)


def urlRedirect(request, slugs):
    slugs="u/" + slugs
    data = UrlData.objects.get(slug=slugs)
    data.count += 1
    data.save()
    #print(data.count)
    return redirect("https://" + data.url)

def url_stats(request):
    data = UrlData.objects.all().order_by('-count')  # Sort by most visited
    return render(request, 'stats.html', {'data': data})



# Create your views here.
