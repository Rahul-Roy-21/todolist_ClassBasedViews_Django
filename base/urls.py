from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskEdit, TaskDelete, Custom_Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Custom_Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<str:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-edit/<str:pk>/', TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<str:pk>/', TaskDelete.as_view(), name='task-delete'),
]