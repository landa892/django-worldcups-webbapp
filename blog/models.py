from django.db import models
from ckeditor.fields import RichTextField

class WorldCup(models.Model):
    year = models.PositiveIntegerField(unique=True)
    host = models.CharField(max_length=100)
    champion = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='worldcups/')
    description = RichTextField()

    def __str__(self):
        return f"{self.year} - {self.champion}"

class Team(models.Model):
    name = models.CharField(max_length=100)
    worldcup = models.ForeignKey(WorldCup, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    photo = models.ImageField(upload_to='players/')
    bio = RichTextField()

    def __str__(self):
        return self.name
