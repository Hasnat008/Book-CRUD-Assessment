from django.shortcuts import render,redirect
from .models import AuthorModel,BookModel
from .forms import AuthorForm,BookForm
from django.db.models import Avg, Min, Max, Count

from django.db.models.functions import ExtractYear


# Create your views here.
def index(request):
    project = BookModel.objects.all()
    Author = AuthorModel.objects.all()
    context = {
        'project':project,
        'Author':Author,
    }
    return render(request,'index.html',context)


def Author_Form(request):
    Author = AuthorForm()
    if request.method == 'POST':
        Author = AuthorForm(request.POST)
        if Author.is_valid():
            Author.save()
            return redirect('index')
    context = {
        'Author':Author,
    }
    return render(request,'Author_Form.html',context)

def book_form(request):
    book_form = BookForm()
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('index')

    context = {
        'book_form': book_form,
    }

    return render(request, 'Book_Form.html', context)





def author_form(request):
    author_form = AuthorForm
    if request.method == 'POST':
        author_form = Author_Form(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('index')

    context = {
        'author_form': author_form,
    }

    return render(request, 'Author_Form.html', context)




def Update_Post(request,pk):
    object = BookModel.objects.get(id=pk)
    book_form = BookForm(instance=object)
    if request.method =='POST':
        book_form = BookForm(request.POST,instance=object)
        if book_form.is_valid():
            book_form.save()
            return redirect('index')

    context = {
        'book_form':book_form
    }
    return render(request,'Book_Form.html',context)



def Update_Author(request,pk):
    auth_obju = AuthorModel.objects.get(id=pk)
    auth_form = AuthorForm(instance=auth_obju)
    if request.method == 'POST':
        auth_form = AuthorForm(request.POST,instance=auth_obju)
        if auth_form.is_valid():
            auth_form.save()
            return redirect('index')

    context = {
        'Author':auth_form
    }
    return render(request,'Author_Form.html',context)




# def delete_Post(request,pk):
#     object = BookModel.objects.get(id=pk)
#     book_form = BookForm(instance=object)
#     if request.method =='POST':
#         book_form = BookForm(request.POST,instance=object)
#         if book_form.is_valid():
#             book_form.delete()
#             return redirect('index')

#     context = {
#         'book_form':book_form
#     }
#     return render(request,'Book_Form.html',context)

def Single_Post(request,pk):
    object = BookModel.objects.get(id=pk)
    context = {
        'object':object
    }
    return render(request,'Single_Post.html',context)


def single_Author(request,pk):
    object = AuthorModel.objects.get(id=pk)
    context = {
        'object':object
    }
    return render(request,'single_Author.html',context)


def delete(request,pk):
    object = BookModel.objects.get(id=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('index')
    context = {
        'awb':object
    }
    return render(request,'delete.html',context)


def delete_Author(request,pk):
    obje = AuthorModel.objects.get(id=pk)
    if request.method == 'POST':
        obje.delete()
        return redirect('index')
    context = {
        'ab':obje
    }
    return render(request,'delete_Author.html',context)


def Aggrigation(request):
    obj = BookModel.objects.all()
    Total_Books = BookModel.objects.aggregate(Count('id'))
    Avg_Price = BookModel.objects.aggregate(average=Avg('Price'))['average']
    Oldest_Book = BookModel.objects.aggregate(Publication_Year__max=Min('Publication_Year'))['Publication_Year__max']
    Newest_Book = BookModel.objects.aggregate(Publication_Year__max=Max('Publication_Year'))['Publication_Year__max']

    bookoneachyear = BookModel.objects.values('Publication_Year').annotate(count=Count('id'))


    context = {
        'total_books': Total_Books,
        'avg_price': Avg_Price,
        'oldest_book_year': Oldest_Book,
        'newest_book_year': Newest_Book,
        'bookoneachyear': bookoneachyear,
    }
    return render(request,'Aggrigation.html',context)
def book_count_per_year(request):
    book_one_each_year = BookModel.objects.values('Publication_Year').annotate(count=Count('id'))
    return render(request, 'Aggrigation.html', {'book_one_each_year': book_one_each_year})