from django.core.validators import EmailValidator, MinValueValidator, RegexValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)]
    )  # for adults? I don't know
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phonenumber = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+?\d{9,15}$",  # just basic validation, I googled it :-D
                message="Phone number must be entered in the format: '+420123456789'. Up to 15 digits allowed.",
            )
        ],
    )

    def __str__(self):
        return self.name


class Website(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    author = models.ForeignKey(
        Author, related_name="websites", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
