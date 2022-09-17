from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=200)
    facebook_link = models.URLField(max_length=100)
    google_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()



    
    

