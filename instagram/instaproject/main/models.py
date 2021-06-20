from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feed(models.Model):
    pub_date=models.DateTimeField('date published')
    text = models.TextField()
    image=models.ImageField(upload_to='photos/%m/%d')

    author= models.ForeignKey(User, related_name='feeds', on_delete= models.CASCADE)


    def __str__(self):
        return "text:" + self.text
    def summary(self):
        return self.text[:100]