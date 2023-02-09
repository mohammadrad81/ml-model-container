from rest_framework import serializers
from .models import MachineLearningModel
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault


class MachineLearningModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MachineLearningModel
        fields = '__all__'
        read_only_fields = ('owner',)