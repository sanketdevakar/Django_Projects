
from django.http import HttpResponse
from django.shortcuts import render

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
