from django.urls import path
from .api_views import RedirectListCreateAPIView, RedirectRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('redirects/', RedirectListCreateAPIView.as_view(), name='api_redirects_list'),
    path('redirects/<slug:slug>/', RedirectRetrieveUpdateDestroyAPIView.as_view(), name='api_redirect_detail'),
]