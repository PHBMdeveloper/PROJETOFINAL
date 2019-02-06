from django.urls import path, include, re_path
from .views import home, contato


urlpatterns = [
    path('', home, name='website_home'),
    path('contato', contato, name='website_contato'),
]
