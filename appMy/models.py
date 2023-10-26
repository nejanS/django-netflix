from django.db import models
from appUser.models import Profile

class Category(models.Model):
    title = models.CharField(("Kategori Başlığı"), max_length=50)

    def __str__(self) -> str:
        return self.title

    class Meta: # Category değişkenlerini alfabetik olarak sıralar
        ordering = ['title']

class Series(models.Model):
   category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.SET_NULL, null=True)
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("Açıklama"), default="")
   image = models.FileField(("Dizi Afişi"), upload_to="series", max_length=100)

   def __str__(self) -> str:
      return self.title
  
class Movies(models.Model):
   category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.SET_NULL, null=True)
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("Açıklama"), default="")
   image = models.FileField(("Film Afişi"), upload_to="movies", max_length=100)

   def __str__(self) -> str:
      return self.title

class Popular(models.Model):
   category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.SET_NULL, null=True)
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("Açıklama"), default="")
   image = models.FileField(("Film Afişi"), upload_to="popular", max_length=100)

   def __str__(self) -> str:
      return self.title

class Netflix(models.Model):
   category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.SET_NULL, null=True)
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("Açıklama"), default="")
   image = models.FileField(("Film Afişi"), upload_to="netflix", max_length=100)

   def __str__(self) -> str:
      return self.title
   
   
class MyList(models.Model):
   profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
   category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.SET_NULL, null=True)
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("Açıklama"), default="")
   image = models.FileField(("Film Afişi"), upload_to="mylist", max_length=100)
   

