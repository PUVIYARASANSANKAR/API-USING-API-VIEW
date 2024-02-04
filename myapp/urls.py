from django.contrib import admin
from django.urls import path
from . import views

from .views import BookAPIView
urlpatterns=[
    path('books/',BookAPIView.as_view(),name='book'),
     path('books/<int:book_id>/', BookAPIView.as_view(), name='book-detail'),
]




