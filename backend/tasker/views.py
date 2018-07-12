from django.http import Http404
from rest_framework import views, viewsets, status
from rest_framework.response import Response

from .models import Project, Country, Operation
from .serializers import ProjectSerializer, CountrySerializer, OperationSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('updated_at')
    serializer_class = ProjectSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('updated_at')
    serializer_class = CountrySerializer


class OperationListView(views.APIView):
    def get(self, request, format=None):
        operations = Operation.objects.all().order_by('updated_at')
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OperationDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Operation.objects.get(pk=pk)
        except Operation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        operation = self.get_object(pk)
        serializer = OperationSerializer(operation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        operation = self.get_object(pk)
        serializer = OperationSerializer(operation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        operation = self.get_object(pk)
        operation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OperationViewSet(viewsets.ViewSet):
    def list(self, request, format=None):
        operations = Operation.objects.all().order_by('updated_at')
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Operation.objects.get(pk=pk)
        except Operation.DoesNotExist:
            raise Http404

    def retrieve(self, request, pk, format=None):
        operation = self.get_object(pk)
        serializer = OperationSerializer(operation)
        return Response(serializer.data)

    def update(self, request, pk, format=None):
        operation = self.get_object(pk)
        serializer = OperationSerializer(operation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        operation = self.get_object(pk)
        operation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
