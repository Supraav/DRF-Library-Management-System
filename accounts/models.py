from django.db import models

# Create your models here.
class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=128)
    MembershipDate = models.DateField(auto_now_add=True)

    class Meta:
        db_table='UserAccounts' 