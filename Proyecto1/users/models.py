from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import User

class UsuarioGeneral(User):
    pass

class UsuarioVerificado(User):
    pass

class Profile (models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio= models.TextField()
    profile_pic=models.ImageField(null=True, blank=True, upload_to="images/profile")
    facebook_url= models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)



    def __str__(self):
        return str(self.user)
