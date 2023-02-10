from django.shortcuts import render, redirect, reverse
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import MachineLearningModel
from .serializers import MachineLearningModelSerializer


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
        serializer.save(owner = self.request.user)

    def get_queryset(self):
        return MachineLearningModel.objects.filter(owner=self.request.user)
