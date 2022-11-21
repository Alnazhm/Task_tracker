from rest_framework import serializers
from todolist.models import Project, Tasks, Status, Type


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'is_deleted', 'tasks']
        read_only_fields = ['is_deleted']


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'name', 'created_at', 'updated_at']


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ['id', 'name', 'created_at', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    type = TypeSerializer(read_only=True)

    class Meta:
        model = Tasks
        fields = ['id', 'summary', 'description', 'is_deleted', 'project', 'status', 'type', 'created_at', 'updated_at']
        read_only_fields = ['is_deleted']