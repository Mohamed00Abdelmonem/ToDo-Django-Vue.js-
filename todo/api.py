from .models import Tasks
from .serializers import TaskSerializer
from rest_framework import generics




class TaskList(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
