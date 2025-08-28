from django.urls import path

# internal imports
from .views import AuthorListCreateView, WebsiteCreateView

urlpatterns = [
    path("author", AuthorListCreateView.as_view(), name="author-list-create"),
    path("website", WebsiteCreateView.as_view(), name="website-create"),
]
