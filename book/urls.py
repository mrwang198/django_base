from django.conf.urls import url
from book.views import index
from django.urls import path

urlpatterns = [
    url(r'^', index)
]

