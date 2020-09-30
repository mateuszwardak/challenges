from django.urls import path

from . import views


urlpatterns = [
    path('datasets/', views.DatasetsView.as_view(), name='datasets'),
    path('dataset/new/', views.NewDataSetView.as_view(), name='new_dataset'),
    path('dataset/<pk>/', views.DatasetView.as_view(), name='dataset'),
]


app_name = 'benfords'
