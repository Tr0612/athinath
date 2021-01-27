from django.db import models
import random
# Create your models here.


class Carousel(models.Model):
    id_image=models.PositiveIntegerField(primary_key=True)
    image=models.ImageField(upload_to='carousel/')

class Category(models.Model):
    category_name=models.CharField(max_length=2000)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    customizationchoices=[
        ('Yes','Yes'),
        ('No','No')
    ]
    product_code=models.CharField(max_length=100)
    product_name=models.CharField(max_length=2000)
    product_description=models.TextField()
    product_min_quantity=models.PositiveIntegerField()
    product_customization=models.CharField(max_length=5,choices=customizationchoices)
    productimage_1=models.ImageField()
    productimage_2=models.ImageField(null=True,blank=True)
    productimage_3=models.ImageField(null=True,blank=True)
    productimage_4=models.ImageField(null=True,blank=True)
    productimage_5=models.ImageField(null=True,blank=True)
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_sub_category=models.CharField(max_length=200)
    added_date=models.DateTimeField(auto_now_add=True)
    def list_item(category):
        items=Product.objects.filter(product_category=Category.objects.get(category_name=category)).order_by(
            '-added_data',
            '-product_prize'
        )

        return items
    def __str__(self):
        return self.product_name

    
    

class Order(models.Model):
    code=models.CharField(max_length=800,unique=True,blank=True,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_quantity=models.PositiveIntegerField()
    customer_name=models.CharField(max_length=256)
    customer_email=models.EmailField()
    customer_number=models.CharField(max_length=10)
    company_name=models.CharField(max_length=300,null=True)
    customer_address=models.TextField(null=True,blank=True)
    order_completed=models.BooleanField()

    def __str__(self):
        return self.customer_name


class Invitations(models.Model):
    Name=models.CharField(max_length=200)
    Number=models.PositiveIntegerField()
    Email=models.EmailField()

    def __str__(self):
        return self.Name




class HomeCategories(models.Model):
    image=models.ImageField(upload_to='categoryimages')
    name=models.OneToOneField(Category,on_delete=models.CASCADE)


class Gifts(models.Model):
    image=models.ImageField(upload_to='Giftimages/')
    Subcategory_name=models.CharField(max_length=100)

    def __str__(self):
        return self.Subcategory_name



class Personalized(models.Model):
    image=models.ImageField(upload_to='Personalized/')
    subcategory_name=models.CharField(max_length=100)

    def __str__(self):
        return self.subcategory_name

    
class Tresures(models.Model):
    image=models.ImageField(upload_to='Tresures/')
    subcategory_name=models.CharField(max_length=100)

    def __str__(self):
        return self.subcategory_name