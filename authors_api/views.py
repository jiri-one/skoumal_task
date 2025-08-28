from rest_framework import generics

# internal imports
from .models import Author, Website
from .serializers import AuthorSerializer, WebsiteSerializer


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all().prefetch_related("websites")
    serializer_class = AuthorSerializer


class WebsiteCreateView(generics.CreateAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
