from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Receta(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = RichTextField(config_name='nombre_referencia',verbose_name="Ingredientes",default='')
    text = RichTextField(config_name='default',verbose_name="Receta")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes= models.ManyToManyField('auth.User', related_name='receta_post')



    def total_likes(self):
        return self.likes.count()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=20)