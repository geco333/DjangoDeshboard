from django.urls import path, include
from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('log/', views.LogView.as_view(), name='log_list'),
    path('log/<int:pk>/', views.LogDetailView.as_view(), name='log_detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
