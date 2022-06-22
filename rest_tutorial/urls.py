from django.contrib import admin
from quickstart import views
from django.urls import include, path


urlpatterns = [
    path('', include('quickstart.urls')),
]

