from django.contrib.auth.models import Group

from .models import User, Task, Organization, Project
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskSerializerList(serializers.ModelSerializer):
    executor = serializers.SlugField()

    class Meta:
        model = Task
        fields = ('title', 'descriptions', 'executor', 'status', 'deadline')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectSerializerList(serializers.ModelSerializer):
    tasks = serializers.SlugField()

    class Meta:
        model = Project
        fields = ('name', 'descriptions', 'status', 'tasks')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

    def create(self, validated_data):
        worker_g = Group.objects.get(name='worker')
        admin_g = Group.objects.get(name='admin')
        user = validated_data.get('admin')

        worker_g.user_set.remove(user)
        admin_g.user_set.add(user)

        user.is_worker = False
        user.is_admin = True
        user.save()

        return Organization.objects.create(**validated_data)


class OrganizationSerializerList(serializers.ModelSerializer):
    project = serializers.SlugField()

    class Meta:
        model = Organization
        fields = ('name', 'project')
