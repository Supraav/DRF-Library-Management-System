from django.contrib import admin
from django.urls import path,include
from accounts.views import UserRegistrationAPIView,UserDeleteView,GetAllUsersAPIView,OneUserDetailsAPIView

urlpatterns = [
    path('register',UserRegistrationAPIView.as_view(),name='register'),
    path('delete/<int:user_id>',UserDeleteView.as_view(),name='delete'),

    path('getall',GetAllUsersAPIView.as_view(),name='getall'),
    path('getone/<int:user_id>', OneUserDetailsAPIView.as_view(), name='user-details'),

    # path('login',TokenAPIView.as_view(),name='login')
]