from django.db import models

# Create your models here.
class tbl_customer(models.Model):
    Username=models.CharField(max_length=100)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Phone=models.IntegerField()
    class meta:
        db_table="tbl_customer"
class tbl_product(models.Model):
    product_photo=models.FileField()
    Product_name=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    Price=models.IntegerField()
    class meta:
        db_table="tbl_product"
class tbl_order(models.Model):
    Product_id=models.IntegerField()
    User_id=models.CharField(max_length=100)
    Product_name=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    Amount=models.IntegerField()
    status=models.CharField(max_length=100)
    class meta:
        db_table="tbl_order"
class tbl_payment(models.Model):
    order_id=models.IntegerField()
    User_id=models.CharField(max_length=500)
    Amount=models.IntegerField()
    Status=models.CharField(max_length=100)
    class meta:
        db_table="tbl_payment"


