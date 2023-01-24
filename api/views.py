from api.serializers import studentsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import students

@api_view(['GET','POST'])
def students_list(request):
    if request.method == 'GET':
        student = students.objects.all()
        serializers = studentsSerializer(student,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        serializers = studentsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


api_view(['GET','PUT','DELETE'])
def students_details(request,pk):
    try:
        student = students.objects.get(pk=pk)
    except students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = studentsSerializer(students)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = studentsSerializer(students,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)