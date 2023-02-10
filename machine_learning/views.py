import pickle

from django.shortcuts import render, redirect, reverse
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import MachineLearningModel
from .serializers import MachineLearningModelSerializer
from . import ml
import uuid
from django.core.files.base import ContentFile, File
import os


class FitView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        x = data['x']
        y = data.get('y', None)
        machine_learning_model = MachineLearningModel.objects.get(pk=pk, owner=self.request.user)
        machine_learning_model.fit(x, y)
        return Response({"message": f"model with id {pk} fitted with data"}, status=status.HTTP_200_OK)


class TransformView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        x = data['x']
        machine_learning_model = MachineLearningModel.objects.get(pk=pk, owner=self.request.user)
        transformed_data = machine_learning_model.transform(x)
        return Response({'result': transformed_data}, status=status.HTTP_200_OK)


class FitTransformView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        x = data['x']
        machine_learning_model = MachineLearningModel.objects.get(pk=pk, owner=self.request.user)
        transformed_data = machine_learning_model.fit_transform(x)
        return Response({'result': transformed_data}, status=status.HTTP_200_OK)


class PredictView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        x = data['x']
        machine_learning_model = MachineLearningModel.objects.get(pk=pk, owner=self.request.user)
        transformed_data = machine_learning_model.predict(x)
        return Response({'result': transformed_data}, status=status.HTTP_200_OK)


class PredictProbaView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        x = data['x']
        machine_learning_model = MachineLearningModel.objects.get(pk=pk, owner=self.request.user)
        transformed_data = machine_learning_model.predict_proba(x)
        return Response({'result': transformed_data}, status=status.HTTP_200_OK)


class CreateMLModelView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MachineLearningModelSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return MachineLearningModel.objects.filter(owner=self.request.user)


class CreateMLModelOnlineView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {"available_models": ml.models_dict.keys()}
        return Response(res, status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        ml_model_algorithm_name = data['ml_model_algorithm']
        ml_model_algorithm = ml.models_dict.get(ml_model_algorithm_name)
        if not os.path.isdir("ml_models"):
            os.makedirs('ml_models')
        address = f'ml_models/{uuid.uuid4()}'
        with open(address, 'wb') as f:
            pickle.dump(ml_model_algorithm, f)
        with open(address, 'rb') as f:
            ml_model = MachineLearningModel.objects.create(name=data['name'],
                                                           owner=self.request.user,
                                                           description=data['description'],
                                                           file=File(f))
        serializer = MachineLearningModelSerializer(instance=ml_model)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DestroyMLModelView(DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MachineLearningModelSerializer

    def get_queryset(self):
        return MachineLearningModel.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])
