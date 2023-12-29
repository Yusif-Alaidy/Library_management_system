from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm, CategoryForm
# Create your views here.

def Home(request):
    context = {
            'category':Category.objects.all(),
            'books':Book.objects.all(),
            'form': BookForm(),
            'cat_form': CategoryForm(),
            'allbooks': Book.objects.filter(active=True).count(),
            'bookssold': Book.objects.filter(status='sold').count(),
            'booksrental': Book.objects.filter(status='rental').count(),
            'bookavalible': Book.objects.filter(status='avalible').count(),
        }
    if request.method == 'POST':
        data = BookForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
        catForm = CategoryForm(request.POST)
        if catForm.is_valid():
            catForm.save()

    return render(request,'pages/index.html', context)


def Books(request):
    
    search = Book.objects.all( )
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    
    context = {
            'category':Category.objects.all(),
            'books': search,
            'cat_form': CategoryForm(),
            

        }
    return render(request,'pages/books.html', context)


def Update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
    update = {
        'book_id':book_save,
    }
    return render(request, 'pages/update.html', update)
    
def Delete(request, id):
    book_delete = Book.objects.get(id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/') 
    
    return render(request, 'pages/delete.html')