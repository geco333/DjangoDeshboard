from django.urls import path, include
from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('genre/', views.GenreView.as_view(), name='genre'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
