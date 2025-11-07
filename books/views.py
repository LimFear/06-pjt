from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Book, Thread
from .forms import BookForm, ThreadForm

# Create your views here.
def index(request):
    books = Book.objects.all()              # 전체 조회
    return render(request, 'books/index.html', {'books': books})  

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('books:detail', book.pk)
    else:
        form = BookForm()
    return render(request, 'books/form.html', {'form': form, 'title': '도서 등록', 'btn': '저장'})


@require_GET
def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    threads = book.threads.all().order_by('-id')
    return render(request, 'books/detail.html', {'book': book, 'threads': threads})


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:detail', book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/form.html', {'form': form, 'title': '도서 수정', 'btn': '수정'})


@require_POST
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('books:index')


@require_http_methods(['GET', 'POST'])
def thread_create(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.book = book
            thread.save()
            return redirect('books:thread_detail', thread.pk)
    else:
        form = ThreadForm()
    return render(request, 'books/thread_form.html', {
        'form': form, 'book': book, 'title': '게시글 작성', 'btn': '저장'
    })


@require_GET
def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    return render(request, 'books/thread_detail.html', {'thread': thread})


@require_http_methods(['GET', 'POST'])
def thread_update(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('books:thread_detail', thread.pk)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'books/thread_form.html', {
        'form': form, 'book': thread.book, 'title': '게시글 수정', 'btn': '수정'
    })


@require_POST
def thread_delete(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    book_pk = thread.book.pk
    thread.delete()
    return redirect('books:detail', book_pk)
