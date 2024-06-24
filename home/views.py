from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def index(request):
    student_obj= Student.objects.all()
    serializers=StudentSerializer(student_obj, many=True)

    return Response({'status':200, 'payload': serializers.data})


@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':400,'errors':serializer.errors, 'message':'something went wrong'})

    serializer.save()
    return Response({'status':200, 'payload':serializer.data})

@api_view(['PUT'])
def update_student(request, id):
    print(f"Request data: {request.data}")  # Log the incoming request data
    
    try:
        student_obj = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({'status': 400, 'message': 'Student not found'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = StudentSerializer(student_obj, data=request.data, partial=True)
    if not serializer.is_valid():
        print(f"Serializer errors: {serializer.errors}")  # Log the errors to console
        return Response({'status': 400, 'errors': serializer.errors, 'message': 'Validation failed'}, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response({'status': 200, 'payload': serializer.data})

@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status': 200,'message': 'Student deleted successfully'})
    
    except Student.DoesNotExist:
        return Response({'status': 403, 'message': 'Student not found'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_books(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj, many=True)
    return Response({'status': 200, 'payload': serializer.data})