from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MachineLearningModel


class FitView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        x = data['x']
        y = data.get('y', None)
        machine_learning_model = MachineLearningModel.objects.get(pk=pk)
        machine_learning_model.fit(x, y)
        return Response({"message": f"model with id {pk} fitted with data"}, status=status.HTTP_200_OK)


class TransformView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        x = data['x']
        machine_learning_model = MachineLearningModel.objects.get(pk=pk)
        transformed_data = machine_learning_model.transform(x)
        return Response({'result': transformed_data}, status=status.HTTP_200_OK)


class FitTransformView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        x = data['x']
        machine_learning_model = MachineLearningModel.objects.get(pk=pk)
        transformed_data = machine_learning_model.fit_transform(x)
        return Response({'result': transformed_data}, status=status.HTTP_200_OK)


class PredictView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        x = data['x']
        machine_learning_model = MachineLearningModel.objects.get(pk=pk)
        transformed_data = machine_learning_model.predict(x)
        return Response({'result': transformed_data}, status=status.HTTP_200_OK)


class PredictProbaView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        x = data['x']
        machine_learning_model = MachineLearningModel.objects.get(pk=pk)
        transformed_data = machine_learning_model.predict_proba(x)
        return Response({'result': transformed_data}, status=status.HTTP_200_OK)
