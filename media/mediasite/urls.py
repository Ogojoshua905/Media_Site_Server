from django.contrib import admin
from django.urls import path, include
from .views import index, home, media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', media, name='media'),
]