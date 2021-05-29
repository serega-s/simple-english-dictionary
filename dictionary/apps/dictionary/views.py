from django.shortcuts import HttpResponse, render
from PyDictionary import PyDictionary


def index(request):
    return render(request, 'index.html')


def word(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        dictionary = PyDictionary()
        meaning = dictionary.meaning(search)
        if meaning:
            synonyms = dictionary.synonym(search)
            antonyms = dictionary.antonym(search)
            context = {
                'meaning': meaning['Noun'][0],
                'synonyms': synonyms,
                'antonyms': antonyms
            }
        else:
            return render(request, '404.html', {'search': search})
    return render(request, 'word.html', context)
