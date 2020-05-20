from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#this class is just additional class for the user to login: the username,
# the email and the password are already in place. since we imported User
#form contrib.auth.models

class UserProfileInfo(models.Model):
    user = models.OneToOneField(
    User, on_delete=models.CASCADE)
    portofolio_site= models.URLField(blank=True)
    profile_pic= models.ImageField(upload_to='profile_pic', blank=True)


    def __str__(self):
        return self.user.username
