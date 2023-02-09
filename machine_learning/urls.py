from django.urls import path
from .views import FitView, FitTransformView, TransformView, PredictView,\
    PredictProbaView, CreateMLModelView, CreateMLModelAccomplishedView

urlpatterns = [
    path('api/fit/<int:pk>/', FitView.as_view(), name='fit'),
    path('api/transform/<int:pk>/', TransformView.as_view(), name='transform'),
    path('api/fit-transform/<int:pk>/', FitTransformView.as_view(), name='fit-transform'),
    path('api/predict/<int:pk>/', PredictView.as_view(), name='predict'),
    path('api/predict-proba/<int:pk>/', PredictProbaView.as_view(), name='predict-proba'),

    path('api/create-ml-model/',
         CreateMLModelView.as_view(),
         name='create-ml-model'),
]