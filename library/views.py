from django.shortcuts import render, redirect, get_object_or_404
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
        form = BookForm(label_suffix='')
    return render(request, 'library/book_new.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
