from django.urls import path, include
from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.LogView.as_view(), name='index'),
    path('log/', views.LogView.as_view(), name='log_list'),
    path('log/<int:pk>/', views.LogDetailView.as_view(), name='log_detail'),
    path('post/', views.SendPost, name='post'),
]
