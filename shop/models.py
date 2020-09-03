from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    # AutoField is auto incrementing field
    product_name = models.CharField(max_length = 50)
    # Default field is necessary
    # Since consider the below field which didn't existed before
    # DB was still maintained before but without the below field
    # So now if we make the migrations the Django will get confused that what should it do to original DB.
    # So we provide a default value to it
    category = models.CharField(max_length = 50, default="")
    subcategory = models.CharField(max_length = 50, default="")
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length = 3000)
    product_pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    # We dont need to make migrations since we have just added a method we have not changed the model anywhere
    # Below method is used to return the name of the Product
    def __str__(self):
        return self.product_name