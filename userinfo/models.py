from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50,null = False)
    def __str__(self):
        return f"{self.category_name}"


class User_info(models.Model):
    name = models.CharField(max_length =100)
    category = models.ForeignKey(Category,on_delete = models.CASCADE,related_name = "category",null = True)
    address = models.CharField(max_length = 100, null = False)
    mail = models.EmailField(unique = True,null = False)
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    user = models.ManyToManyField(User_info,null=True)
    product_name = models.CharField(max_length = 100,null = True)
    