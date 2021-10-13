from django.shortcuts import render, HttpResponse, redirect

from app01.models import *


# Create your views here.
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        authors_id_list = request.POST.getlist('authors_id_list')  # checkbox,select
        publish_id = request.POST.get('publish_id')

        # 添加书籍记录，一对多
        book_obj = Book.objects.create(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
        # 添加书籍对应作者，多对多
        book_obj.authors.add(*authors_id_list)
        return redirect('/books')

    publish_list = Publish.objects.all()
    author_list = Author.objects.all()

    return render(request, 'addbook.html', locals())


def books(request):
    book_list = Book.objects.all()
    return render(request, 'books.html', locals())


def change_book(request, edit_book_id):
    book_obj = Book.objects.filter(nid=edit_book_id).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        authors_id_list = request.POST.getlist('authors_id_list')  # checkbox,select
        publish_id = request.POST.get('publish_id')
        # 更新书籍记录
        Book.objects.filter(nid=edit_book_id).update(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
        # 更新作者
        # book_obj.authors.clear()
        # book_obj.authors.add(*authors_id_list)
        book_obj.authors.set(authors_id_list)  # 先清空，再设置

        return redirect('/books')

    author_list = Author.objects.all()
    publish_list = Publish.objects.all()
    return render(request, 'editbook.html', locals())


def delete_book(request, delete_book_id):
    Book.objects.filter(nid=delete_book_id).delete()
    return redirect('/books')
