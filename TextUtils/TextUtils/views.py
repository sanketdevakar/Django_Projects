# I have created this file - Sanket
from django.http import HttpResponse
from django.shortcuts import render

# Code for Practice
'''
def index(request):
    file = open("TextUtils\one.txt","r+")
    return HttpResponse(file.read())

def about(request):
    return HttpResponse("About User")

def ex1(request):
    s = <h1> Navigate Different Websites <br> </h1>
    <a href ="https://www.youtube.com/"> Youtube </a><br>
    <a href ="https://www.oed.com/?tl=true"> Oxford Dictionary </a><br>
    <a href ="https://www.facebook.com/?_rdr"> Facebook </a><br>
    <a href ="https://www.espncricinfo.com/"> ESPN Cricket Info </a><br>
    <a href ="https://www.flipkart.com/">  Flipkart </a><br>
    return HttpResponse(s)
'''

# Code for creating a pipeline

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the Text
    djtext = request.POST.get('text', 'default')

    # Get the status of checkboxes
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}

        djtext = analyzed

    if capitalize == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Capitalizing all words", 'analyzed_text': analyzed}

        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': "Removing the new lines", 'analyzed_text': analyzed}

        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ''
        for index,char in enumerate(djtext):
            if not( djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyzed = analyzed + char
        
        params = {'purpose': "Removing the extra spaces", 'analyzed_text': analyzed}

        djtext = analyzed

    if charcount == 'on':

        
        analyzed = f"Analyzed text = {djtext}. It contains {len(str(djtext))} characters"
        
        params = {'purpose': "Count the number of characters", 'analyzed_text': analyzed}

        djtext = analyzed

        
    if (removepunc == 'off' and capitalize == 'off' and newlineremover == 'off' and extraspaceremover == 'off') :
        return HttpResponse("Please select any operation and try again")
    
    return render(request, 'analyze.html', params)


'''
def capfirst(request):
    return HttpResponse("capitalize first <a href='/'> Back </a>")

def newlineremove(request):
    return HttpResponse("New line remover <a href='/'> Back </a>")


def spaceremove(request):
    return HttpResponse("space remover <a href='/'> Back </a>")

def charcount(request):
    return HttpResponse("charcount <a href='/'> Back </a>")

'''