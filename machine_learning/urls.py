from django.urls import path
from .views import FitView, FitTransformView, TransformView, PredictView,\
    PredictProbaView, CreateMLModelView, CreateMLModelOnlineView, DestroyMLModelView,\
    ListMLModelView, DownloadMLModelView

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
    path('list-ml-model/',
         ListMLModelView.as_view(),
         name='list-ml-model'),
    path('download-ml-model/<int:pk>/',
         DownloadMLModelView.as_view(),
         name='download-ml-model')
]