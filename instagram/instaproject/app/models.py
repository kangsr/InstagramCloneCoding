from django.db import models

# Create your models here.
class Feed(models.Model):
    pub_date= models.DateTimeField('date published')#최초 저장시만 현재날짜 사용
    text= models.TextField()
    image = models.ImageField(upload_to='photos/%m/%d')#월,날짜 폴더에 저장

    def __str__(self):
        return "text:" + self.text
    def summary(self):
        return self.text[:100]