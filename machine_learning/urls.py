from django.urls import path
from .views import FitView, FitTransformView, TransformView, PredictView,\
    PredictProbaView, CreateMLModelView, CreateMLModelOnlineView, DestroyMLModelView

urlpatterns = [
    path('fit/<int:pk>/', FitView.as_view(), name='fit'),
    path('transform/<int:pk>/', TransformView.as_view(), name='transform'),
    path('fit-transform/<int:pk>/', FitTransformView.as_view(), name='fit-transform'),
    path('predict/<int:pk>/', PredictView.as_view(), name='predict'),
    path('predict-proba/<int:pk>/', PredictProbaView.as_view(), name='predict-proba'),

    path('create-ml-model/',
         CreateMLModelView.as_view(),
         name='create-ml-model'),
    path('create-ml-model-online/', CreateMLModelOnlineView.as_view(),
         name='create-ml-model-online'),
    path('delete-ml-model/<int:pk>/',
         DestroyMLModelView.as_view(),
         name='delete-ml-model'),
]