from django.db import models

# Create your models here.
class Customer(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 59)

 