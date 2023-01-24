from rest_framework import serializers
from api.models import students

class studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields=[
            "id",
            "fname",
            "lname",
            "nrc",
            "results",
        ]