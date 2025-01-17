from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)


    class Meta:
        db_table='category'

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    Img=models.ImageField(upload_to='image',default='')
    p_name=models.CharField(max_length=30)
    p_price=models.IntegerField()
    p_description=models.TextField(max_length=300)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)



    class Meta:
        db_table='product'
    
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    

    class Meta:
        db_table='cart'

    # def __str__(self):
    #     return self.product.p_name     





              

      

