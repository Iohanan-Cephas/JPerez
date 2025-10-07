from rest_framework import generics
from .models import Redirect
from .serializers import RedirectSerializer

class RedirectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer

class RedirectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer
    lookup_field = 'slug'
