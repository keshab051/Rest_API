from django.db import models

# Create your models here.

class Moviedata(models.Model):
    
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    # field to catgorize the movie type
    typ = models.CharField(max_length=200,default='action')