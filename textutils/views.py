#I have created this file - Subodh
from django.http import HttpResponse
from django.shortcuts import render
#pipeline concept
def index(request):
    return render(request, 'index.html')

    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.GET.get('text', 'default')
    #checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        #analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params )
    if (fullcaps == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper Case', 'analyzed_text': analyzed}
        # analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        # analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):

                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        # analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (extraspaceremover != 'on'and newlineremover != 'on' and fullcaps != 'on' and removepunc != "on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)

