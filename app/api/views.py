from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from todolist.models import Project, Tasks
from api.serializers import ProjectSerializer, TaskSerializer


class TaskDetailView(APIView):

    def get(self, request, *args, **kwargs):
        objects = Tasks.objects.filter(id=kwargs['pk'])
        serializer = TaskSerializer(objects, many=True)
        return Response(serializer.data)


class ProjectDetailView(APIView):

    def get(self, request, *args, **kwargs):
        objects = Project.objects.filter(id=kwargs['pk'])
        serializer = ProjectSerializer(objects, many=True)
        return Response(serializer.data)


class ProjectUpdateView(APIView):

    def get_object(self, pk):
        return Project.objects.get(pk=pk)


    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = ProjectSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data="wrong parameters")


class TaskUpdateView(APIView):

    def get_object(self, pk):
        return Tasks.objects.get(pk=pk)

    def put(self, request, pk):
        object = self.get_object(pk)
        serializer = TaskSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data="wrong parameters")


class ProjectDeleteView(APIView):

    def get_object(self, pk):
            return Project.objects.get(pk=pk)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(data={"id": event.id})


class TaskDeleteView(APIView):

    def get_object(self, pk):
            return Tasks.objects.get(pk=pk)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(data={"id": event.id})