from django.urls import path
from api.views import ProjectDetailView, TaskDetailView, ProjectUpdateView, \
    TaskUpdateView, ProjectDeleteView, TaskDeleteView


urlpatterns = [
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete')

]