from rest_framework import serializers

# internal imports
from .models import Author, Website


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ["id", "name", "url", "author"]
        extra_kwargs = {"author": {"write_only": True}}


class WebsiteShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ["id", "name", "url"]


class AuthorSerializer(serializers.ModelSerializer):
    websites = WebsiteShortSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "age", "email", "phonenumber", "websites"]
