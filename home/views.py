from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
import pandas as pd
import uuid
# Create your views here.

# @api_view(['GET'])
# def index(request):
#     student_obj= Student.objects.all()
#     serializers=StudentSerializer(student_obj, many=True)

#     return Response({'status':200, 'payload': serializers.data})


# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data=request.data)

#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status':400,'errors':serializer.errors, 'message':'something went wrong'})

#     serializer.save()
#     return Response({'status':200, 'payload':serializer.data})

# @api_view(['PUT'])
# def update_student(request, id):
#     print(f"Request data: {request.data}")  # Log the incoming request data
    
#     try:
#         student_obj = Student.objects.get(id=id)
#     except Student.DoesNotExist:
#         return Response({'status': 400, 'message': 'Student not found'}, status=status.HTTP_400_BAD_REQUEST)

#     serializer = StudentSerializer(student_obj, data=request.data, partial=True)
#     if not serializer.is_valid():
#         print(f"Serializer errors: {serializer.errors}")  # Log the errors to console
#         return Response({'status': 400, 'errors': serializer.errors, 'message': 'Validation failed'}, status=status.HTTP_400_BAD_REQUEST)

#     serializer.save()
#     return Response({'status': 200, 'payload': serializer.data})

# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status': 200,'message': 'Student deleted successfully'})
    
#     except Student.DoesNotExist:
#         return Response({'status': 403, 'message': 'Student not found'}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def get_books(request):
#     book_obj = Book.objects.all()
#     serializer = BookSerializer(book_obj, many=True)
#     return Response({'status': 200, 'payload': serializer.data})


class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':400,'errors':serializer.errors, 'message':'something went wrong'})

        serializer.save()
        return Response({'status':200, 'payload':serializer.data})

    
    def patch(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)
            if not serializer.is_valid():
                print(f"Serializer errors: {serializer.errors}")  # Log the errors to console
                return Response({'status': 400, 'errors': serializer.errors, 'message': 'Validation failed'})

            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        except Student.DoesNotExist:
            return Response({'status': 400, 'message': 'Student not found'})
    
    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({'status': 200,'message': 'Student deleted successfully'})
        
        except Student.DoesNotExist:
            return Response({'status': 403, 'message': 'Student not found'})


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':400,'errors':serializer.errors, 'message':'something went wrong'})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'status':200, 'payload':serializer.data, 'refresh': str(refresh),
        'access': str(refresh.access_token)})


class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentGeneric1(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


class ExportImportExcel(APIView):
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)

        df = pd.DataFrame(serializer.data)
        print(df)
        df.to_csv(
            f'{uuid.uuid4()}.csv', 
            encoding='UTF-8')
        return Response({'status': 200})
    
    def post(self, request):
        # excel_updload_obj = ExelFileUpload.objects.create(excel_file_updload=request.FILES[''])
        # df = pd.read_csv(f'{excel_updload_obj.excel_file_updload}')
        # print(df.values.tolist())
        # print(request.FILES)

        return Response({'status': 200})