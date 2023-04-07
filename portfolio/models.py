from django.db import models


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=50)
    img_link = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Projects(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    git_link = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Suggestions(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} {self.surname} - {self.phone_number}'

