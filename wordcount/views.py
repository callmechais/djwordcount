from django.shortcuts import render

def home(request):
    return render(request, 'word.html',{"counttext":"100"})

def wordcount(request):
    words = request.GET['fulltext']
    wordlist = words.split(' ')
    return render(request, 'count.html',
                  {'words':words, "len":len(wordlist)})

def help(request):
    return render(request, 'help.html')