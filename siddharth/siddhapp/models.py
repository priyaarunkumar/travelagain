from django.db import models

# Create your models here.
class travel(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pic')
    desc=models.TextField()
    def __str__(self):
        return self.name
class cricket(models.Model):
    na=models.CharField(max_length=250)
    im=models.ImageField(upload_to='pic')
    des=models.TextField()
    def __str__(self):
        return self.na

