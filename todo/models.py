from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager



STATUS_TASK = {
    'todo': 'todo',
    'inprogress': 'inprogress',
    'finished': 'finished',
}

class Tasks(models.Model):
    user = models.ForeignKey(User, related_name = 'user_task', on_delete= models.CASCADE)
    task = models.TextField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_TASK.items())
    created_at = models.DateTimeField(timezone.now)
    tags = TaggableManager()

    def __str__(self):
        return self.task
    



