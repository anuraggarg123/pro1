from django.db import models
class Category(models.Model):
    objects = None
    title= models.CharField(max_length=30)
    desc = models.TextField()
    def __str__(self):
        return self.title

class Image(models.Model):
    objects = None
    title = models.CharField(max_length=90)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')
    date = models.DateTimeField()
    categ = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title