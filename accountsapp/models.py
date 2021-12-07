from django.db import models

# Create your models here.
class registertble(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50,unique=True)
    paswd = models.CharField(max_length=32)
    repaswd = models.CharField(max_length=32)
    chk_box = models.BooleanField(default=False)
    def __str__(self):
        return self.fullname

