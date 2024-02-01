
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status,serializers
from rest_framework.permissions import AllowAny,IsAuthenticated
from books.models import Book, BookDetails,BorrowedBooks
from books.serializers import BookSerializer,BookDetailSerializer,BorrowBookSerializer,BorrowBookReturnSerializer

# Create your views here.

#add book
class AddBookView(GenericAPIView):
    serializer_class = BookSerializer
    def post(self,request):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg': 'Something went wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#get all books
class GetAllBooksView(GenericAPIView):
    serializer_class = BookSerializer
    def get(self,request):
        try:
            books=Book.objects.all()
            serializer=BookSerializer(books,many=True)
            return Response({"Books": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'msg': 'Something went wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#get one book
class GetOneBookView(GenericAPIView):
    serializer_class = BookDetailSerializer
    def get(self,request,book_id):
        try:
            books=Book.objects.get(BookID=book_id)
            if books:
                try:
                    bookdetail=BookDetails.objects.get(Book_id=books)
                except:return Response({"msg":'book details not entered for this ID'}, status=status.HTTP_404_NOT_FOUND)

                if bookdetail:
                    serializer=BookDetailSerializer(bookdetail)
                    return Response({"Books": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"msg":'book not found for the requested ID'}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({'msg': 'Something went wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#create/update existing book
class AssignUpdateBookView(GenericAPIView):
    serializer_class = BookDetailSerializer
    def post(self,request,book_id):
        try:
            book=Book.objects.get(BookID=book_id)
            if book:
                serializer=BookDetailSerializer(data=request.data)

                if serializer.is_valid(raise_exception=True):
                    serializer.save(Book=book)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'msg': 'Book not found from DB'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'msg': 'Something went wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,book_id):
        try:
            book=Book.objects.get(BookID=book_id)
            if book:
                bookdetails=BookDetails.objects.get(Book_id=book_id)

                if bookdetails:
                    serializer=BookDetailSerializer(bookdetails,data=request.data,partial=True)

                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'msg': 'Book not found from DB'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'msg': 'Something went wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
#borrow book
class BorrowBookView(GenericAPIView):
    serializer_class = BorrowBookSerializer
    def post(self,request):
        try:
            serializer = BorrowBookSerializer(data=request.data,many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'msg': 'Something went wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
#return book
class ReturnBookView(GenericAPIView):
    serializer_class = BorrowBookReturnSerializer
    def post(self,request,borrowed_book_id):
        userid=request.data.get('user')
        try:
            book=Book.objects.get(BookID=borrowed_book_id)
            if book:
                borrowedbook = BorrowedBooks.objects.get(book_id=borrowed_book_id, user_id=userid,ReturnDate__isnull=True)
                if borrowedbook:
                    borrowedbook.ReturnDate = request.data.get('ReturnDate')
                    borrowedbook.save()
                    return Response({'msg': 'Book returned successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({"msg": "The book is not borrowed by the current user"},
                                    status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({"msg":"the book doesnot exist with this ID"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'msg': 'Something went wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#list all currently borrowed books
class ListAllBorrowedBooksView(GenericAPIView):
    serializer_class = BorrowBookSerializer
    def get(self, request):
        borrowed_books = BorrowedBooks.objects.filter(ReturnDate__isnull=True)
        serializer = BorrowBookSerializer(borrowed_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)