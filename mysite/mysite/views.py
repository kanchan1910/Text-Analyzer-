# views.py
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    wordcounter =request.GET.get('wordcounter', 'off')

    if(removepunc== "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        djtext = analyzed


    if(extraspaceremover == "on"):
        analyzed = ""
        for index in range(len(djtext) - 1):
            if(not(djtext[index] == ' ' and djtext[index + 1] == ' ')):
                analyzed = analyzed + djtext[index]
        params = {'analyzed_text': analyzed}
        djtext = analyzed


    if(wordcounter == "on"):
        count = 0
        for word in djtext.split():
            count = count + 1
        params = {'analyzed_text': count}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and wordcounter != "on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)