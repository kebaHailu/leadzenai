from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/edit/', views.updateTask , name='edit-todo'),
    path('<int:pk>/delete/', views.deleteTask , name='delete-todo'),
    path('deleteall/', views.deleteAll , name='delete-all')
]

