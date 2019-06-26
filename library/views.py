from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        book = form.save(commit=False)
        book.save()
        return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_new.html', {'form': form})