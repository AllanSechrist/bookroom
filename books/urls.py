from django.urls import path

from .views import BookListView, BookDetail

urlpatterns = [
    path("<int:pk>/", BookDetail.as_view(), name="book_detail"),
    path("", BookListView.as_view(), name="book_list"),
]
