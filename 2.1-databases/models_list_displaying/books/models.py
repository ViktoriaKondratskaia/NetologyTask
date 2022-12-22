# coding=utf-8
from django.shortcuts import render
from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')

    def __str__(self):
        return self.name + " " + self.author

def books(request, data):
    template = 'books/books_list.html'
    data = Book.objects.filter(pub_date=data).all()
    next_date = Book.objects.filter(pub_date__gt=data).order_by('pub_date').values_list('pub_date', flat = True).first()
    previous_date = Book.objects.filter(pub_date__lt=data).order_by('pub_date').values_list('pub_date', flat = True).first()
    context = {'books.next_date': next_date,
               'books.previous_date': previous_date}
    return render(request, template, context)




