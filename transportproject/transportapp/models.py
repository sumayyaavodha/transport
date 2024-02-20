from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pictures')
    desc=models.TextField()

    def __str__(self):
        return self.name

class guys(models.Model):
    img=models.ImageField(upload_to='pictures')
    name=models.CharField(max_length=250)
    desc=models.TextField()