from rest_framework import status
from .permissions import CUDModelPermissions
from .serializers import TaskSerializer, TaskSerializerList, \
    OrganizationSerializer, OrganizationSerializerList, \
    ProjectSerializer, ProjectSerializerList
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import RegistrationSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (CUDModelPermissions,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TaskSerializerList
        else:
            return TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = (CUDModelPermissions,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProjectSerializerList
        else:
            return ProjectSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Organization.objects.all()
    permission_classes = (CUDModelPermissions,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrganizationSerializerList
        else:
            return OrganizationSerializer
