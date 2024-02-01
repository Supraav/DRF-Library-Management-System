from django.db import models
from accounts.models import User

# Create your models here.

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13, unique=True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=50)

    class Meta:
        db_table='Book'

class BookDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    Book = models.OneToOneField(Book, on_delete=models.CASCADE)
    NumberOfPages = models.IntegerField()
    Publisher = models.CharField(max_length=100)
    Language = models.CharField(max_length=50)

    class Meta:
        db_table='BookDetails' 

class BorrowedBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)

    class Meta:
        db_table='BorrowedBooks' 
