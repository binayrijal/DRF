from .models import Student
from rest_framework import serializers


def namestartwith_a(value):

  if value[0].lower()!='a':
    raise serializers.ValidationError('name  start with a')
  return value

 
      

class StudentSerializer(serializers.ModelSerializer):
  name=serializers.CharField(validators=[namestartwith_a])
  class Meta:
    model=Student
    fields='__all__'
    read_only_fields=['name']
    extra_kwargs={'name':{'read_only':True}}

    """class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[namestartwith_a])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    
    def create(self, validated_data):
     return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
     instance.name=validated_data.get('name',instance.name)
     instance.roll=validated_data.get('roll',instance.roll)
     instance.city=validated_data.get('city',instance.city)
     instance.save()
     return instance"""
    
    #field level validato
    def validate_roll(self,value):
      if value>=200:
        raise serializers.ValidationError('roll must be less than 200')
      return value
    
    #object validator
    def validate(self, data):
      nm=data.get('name')
      ct=data.get('city')
      sut=Student.objects.all()
      for student in sut:
       dname=student.name.lower()
       dcity=student.city.lower()
       if nm.lower()==dname and ct.lower()== dcity :
        raise serializers.ValidationError('both are already exists')
      return data      
  