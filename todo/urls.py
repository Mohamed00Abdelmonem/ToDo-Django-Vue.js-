from django.urls import path
from .api import TaskList

app_name = 'todo'

urlpatterns = [
    path('api/', TaskList.as_view()),


]