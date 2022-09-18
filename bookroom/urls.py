from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/books/", include("books.urls")),
    path("api/v1/rooms/", include("rooms.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
