from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer = models.CharField(max_length=255)
    img = models.ImageField(upload_to ='upload', blank= True,null =True)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    delivery_address = models.CharField(max_length=255)

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





