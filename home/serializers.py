from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = ['name', 'age']
        fields = '__all__'
    
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError('Age should be greater than 18')
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError('Name should not contain digits')
                
        
        
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name',]
    
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1
