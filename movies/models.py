from django.db import models
from django.contrib.auth.models import User
from datetime import date



# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=50, blank=True, null=True)
    cover = models.ImageField(upload_to='covers/')
    description = models.TextField(blank=True, null=True)
    trailer = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name
    

class Person(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='actors/',blank=True,null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    @property
    def age(self):
        if not self.date_of_birth:
            return None
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def __str__(self):
        return self.name
    

class MovieCredit(models.Model):
    ROLE_CHOICES = [
        ('actor', 'Actor'),
        ('director', 'Director'),
        ('producer', 'Producer'),
        ('writer', 'Writer'),
    ]

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='credits')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    character_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('movie', 'person', 'role')

    def __str__(self):
        return f"{self.person.name} - {self.role}"

