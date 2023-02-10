from rest_framework import serializers
from .models import MachineLearningModel
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault


class MachineLearningModelSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)
    owner = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = MachineLearningModel
        fields = '__all__'
