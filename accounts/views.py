
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import UserRegisterSerializer,UsersSerializer
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

# Create your views here.

#register User
class UserRegistrationAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer
    def post(self, request):
        try:
            serializer = UserRegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                                serializer.data, 
                                status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg': 'Something went wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# DELETE the USER
class UserDeleteView(GenericAPIView):
    def delete(self,request,user_id):
        try:
            user=User.objects.get(UserID=user_id)
            if user:
                user.delete()
                return Response({'msg': 'User deleted successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
                return Response({'msg': 'User doesnot exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'msg': 'Something went wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#get all users
class GetAllUsersAPIView(GenericAPIView):
    serializer_class = UsersSerializer
    def get(self, request):
        try:
            users=User.objects.all()
            serializer = UsersSerializer(users,many=True)
            return Response({"Info": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg': 'Something went wrong', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# get one user
class OneUserDetailsAPIView(GenericAPIView):
    serializer_class = UsersSerializer
    def get(self, request, user_id):
        try:
            user = User.objects.get(UserID=user_id)
            serializer = UsersSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# #Login User
# class TokenAPIView(GenericAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserLoginSerializer
#     def post(self, request):
#         email = request.data.get('Email')
#         password = request.data.get('Password')

#         try:
#             user = User.objects.get(Email=email)
#         except User.DoesNotExist:
#             return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

#         if check_password(password, user.Password):

#             # Generate JWT tokens
#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)

#             return Response({'access_token': access_token,'refresh_token':str(refresh)}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
