from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):  # create a model user with additional fields like profile pic etc
    usr = models.OneToOneField(User,on_delete = User) # one to one mapping for re-use django's User Model
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = "Profile Pictures/",blank  = True)

    def __str__(self):
        return self.usr.username
