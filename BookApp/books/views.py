from django.shortcuts import render

from .models import Books

from .vector_search import search_vector
from .books_search import search_books

# Create your views here.

def search_view(request, *args, **kwargs):
    return render(request, 'index.html', {})

def search_result(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        isbns = search_vector(searched)
        books = search_books(isbns)
        context = {'searched': searched,
        'books': books}
        return render(request, 'search_result.html', context)
    else:
        context = {}
        return render(request, 'search_result.html', context)
    