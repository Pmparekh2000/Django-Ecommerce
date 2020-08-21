from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    # AutoField is auto incrementing field
    product_name = models.CharField(max_length = 50)
    product_desc = models.CharField(max_length = 300)
    product_pub_date = models.DateField()