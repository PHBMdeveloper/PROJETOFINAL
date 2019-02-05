from django.urls import path, include, re_path
from .views import home


urlpatterns = [
    path('', home, name='website_home'),
]