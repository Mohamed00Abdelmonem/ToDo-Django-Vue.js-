from .models import Tasks
from .serializers import TaskSerializer
from rest_framework import generics




class TaskList(generics.ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
