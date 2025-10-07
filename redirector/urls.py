from django.urls import path

from .views import HomeView, RedirectSlugView, EditRedirectView, DeleteRedirectView

urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    path('r/<slug:slug>/', RedirectSlugView.as_view(), name='redirect'),
    path('edit/<int:id>/', EditRedirectView.as_view(), name='edit_redirect'),
    path('delete/<int:id>/', DeleteRedirectView.as_view(), name='delete_redirect'),
]