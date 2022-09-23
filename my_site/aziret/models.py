from django.db import models

# Create your models here.



class Category (models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name




class Peoples (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True ,null=True)
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=120)
    content = models.TextField()
    years = models.IntegerField()
    img = models.ImageField(upload_to ='upload', blank= True,null =True)
    
    def __str__(self):
        return self.category
    def __str__(self):
        return self.title
    def __str__(self):
        return self.sub_title
    def __str__(self):
        return self.content


class News(models.Model):
    title =   models.CharField(max_length=120)
    imgs = models.ImageField(upload_to ='upload', blank= True,null =True)
    body = models.TextField()
    avtor=models.TextField()