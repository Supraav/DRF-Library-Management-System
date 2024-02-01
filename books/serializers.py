from rest_framework import serializers
from accounts.models import User
from books.models import Book,BookDetails,BorrowedBooks

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookDetails
        fields=['DetailsID','NumberOfPages','Publisher','Language','Book_id']

class BorrowBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BorrowedBooks
        fields=['id','BorrowDate','user','book']
        read_only_fields = ['id']

class BorrowBookReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model=BorrowedBooks
        fields=['id','ReturnDate','user']
        read_only_fields = ['id']