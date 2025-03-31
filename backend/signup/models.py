from django.db import models

# Create your models here.
class newuser(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    mobilenum=models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.email