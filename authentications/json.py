from .models import User,Person,Company
from rest_framework import serializers 
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()



#auth


class  jsonUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class  jsonPerson(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

class  jsonCompany(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"