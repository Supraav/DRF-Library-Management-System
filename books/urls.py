from django.urls import path,include
from books.views import (AddBookView,
                        GetAllBooksView,
                        GetOneBookView,
                        AssignUpdateBookView,
                        BorrowBookView,
                        ReturnBookView,
                        ListAllBorrowedBooksView)

urlpatterns = [
    path('addbook',AddBookView.as_view(),name='add_book'),
    path('listallbooks',GetAllBooksView.as_view(),name='getallbooks'),
    path('getonebookdetails/<int:book_id>',GetOneBookView.as_view(),name='getonebook'),
    path('modifybook/<int:book_id>',AssignUpdateBookView.as_view(),name='modifybook'),
    path('borrowbook',BorrowBookView.as_view(),name='borrowbook'),
    path('returnbook/<int:borrowed_book_id>',ReturnBookView.as_view(),name='returnbook'),
    path('listborrowedbook',ListAllBorrowedBooksView.as_view(),name='list-borrowed-books'),
]