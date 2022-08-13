from django.conf.urls import url
from book.views import index,bookList
from django.urls import path


urlpatterns = [
    url(r'^booklist/$', bookList),
    url(r'^$', index),
]

