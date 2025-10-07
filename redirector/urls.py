from django.urls import path

from .views import home, redirect_slug, edit_redirect, delete_redirect

urlpatterns =[
    path('', home, name='home'),
    path('r/<slug:slug>/', redirect_slug, name='redirect'),
    path('edit/<int:id>/', edit_redirect, name='edit_redirect'),
    path('delete/<int:id>/', delete_redirect, name='delete_redirect'),
]