from django.urls import path
from tasks.views import TaskViewSet, TaskStatusUpdateView

urlpatterns = [
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task-list'),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='task-detail'),
    path('tasks/<int:pk>/update-status/', TaskStatusUpdateView.as_view(), name='task-update-status'),
]
