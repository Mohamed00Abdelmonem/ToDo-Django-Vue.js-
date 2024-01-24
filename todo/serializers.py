from rest_framework import serializers
from .models import Tasks

from taggit.serializers import (TagListSerializerField, TaggitSerializer)
                          


class TaskSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Tasks   
        fields = ['user', 'task', 'tags', 'status', 'created_at']

