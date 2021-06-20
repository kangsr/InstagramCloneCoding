from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH, related

class Profile(models.Model):
    user= models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)#1:1관계
    profileImg = models.ImageField(upload_to = 'profileImg', blank = True)
    nickName = models.CharField(max_length=20, blank=True)
    intro = models.TextField(blank=True)


