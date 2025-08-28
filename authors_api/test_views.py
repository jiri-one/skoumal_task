from typing import Any

import pytest
from django.urls import reverse
from rest_framework import status

# internal imports
from .models import Author, Website


@pytest.mark.django_db
def test_create_author(client):
    url = reverse("author-list-create")
    data: dict[str, Any] = {
        "name": "Jan Novak",
        "age": 32,
        "email": "jan@example.com",
        "phonenumber": "+420123456789",
    }
    response = client.post(url, data, content_type="application/json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == "Jan Novak"


@pytest.mark.django_db
def test_list_authors_and_websites(client):
    name = "Jana"
    age = 29
    email = "jana@x.cz"
    phonenumber = "+420123456789"
    website_name = "Jana Site"
    website_url = "https://jana.cz"

    author = Author.objects.create(
        name=name, age=age, email=email, phonenumber=phonenumber
    )
    Website.objects.create(name=website_name, url=website_url, author=author)
    url = reverse("author-list-create")
    response = client.get(url)
    # response check
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    # author check
    assert response.data[0]["name"] == name
    assert response.data[0]["age"] == age
    assert response.data[0]["email"] == email
    assert response.data[0]["phonenumber"] == phonenumber
    # website check
    assert response.data[0]["websites"][0]["name"] == website_name
    assert response.data[0]["websites"][0]["url"] == website_url


@pytest.mark.django_db
def test_create_website(client):
    author = Author.objects.create(
        name="Petr", age=40, email="petr@x.cz", phonenumber="+420123456787"
    )
    website_name = "Petrův blog"
    website_url = "http://petr.cz"
    url = reverse("website-create")
    data = {"name": website_name, "url": website_url, "author": author.id}
    response = client.post(url, data, content_type="application/json")
    # check response itself
    assert response.status_code == status.HTTP_201_CREATED
    # check some response data
    assert response.data["name"] == website_name
    # check if all is in DB
    website = Website.objects.get(name=website_name)
    assert website.name == website_name
    assert website.url == website_url
    assert website.author == website.author


# AND HERE SOME NEGATIVE TESTS OF VALIDATORS


@pytest.mark.django_db
def test_invalid_email(client):
    url = reverse("author-list-create")
    data = {
        "name": "Bad Email",
        "age": 22,
        "email": "not-an-email",
        "phonenumber": "+420123456780",
    }
    response = client.post(url, data, content_type="application/json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_invalid_phonenumber(client):
    url = reverse("author-list-create")
    data = {
        "name": "Bad Phone",
        "age": 22,
        "email": "phone@example.com",
        "phonenumber": "abcdefg",
    }
    response = client.post(url, data, content_type="application/json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_min_age_constraint(client):
    url = reverse("author-list-create")
    data = {
        "name": "Too Young",
        "age": 5,
        "email": "young@example.com",
        "phonenumber": "+420123456781",
    }
    response = client.post(url, data, content_type="application/json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


# AND ONE MORE NEGATIVE TEST FOR NON-EXISTENT AUTHOR


@pytest.mark.django_db
def test_create_website_without_author(client):
    # Try to create a website with a non-existent author ID
    bad_author_id = 9999
    url = reverse("website-create")
    data = {
        "name": "Ghost Blog",
        "url": "https://ghost.cz",
        "author": bad_author_id,
    }
    response = client.post(url, data, content_type="application/json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "author" in response.data
    assert (
        str(response.data["author"][0])
        == f'Invalid pk "{bad_author_id}" - object does not exist.'
    )
