from django.urls import path
from . import views

    

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('create-user/', views.createUser, name= 'create-user'),
    path('update-user/<str:pk>', views.updateUser, name= 'update-user'),
    path('create-task/', views.createTask, name= 'create-task'),
    path('update-task/<str:pk>', views.updateTask, name= 'update-task'),
    path('create-comment/', views.createComment, name= 'create-comment'),
]
