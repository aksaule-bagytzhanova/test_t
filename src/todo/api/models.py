import time
from datetime import datetime, timedelta
import jwt
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
    PermissionsMixin, Group)

from rest_framework.permissions import IsAuthenticated


class UserManager(BaseUserManager):

    def add_to_group(self, user):
        root_admin = Group.objects.get(name='root_admin')
        admin = Group.objects.get(name='admin')
        worker = Group.objects.get(name='worker')

        if user.is_root_admin or user.is_superuser:
            root_admin.user_set.add(user)
            print("Add to root admin")
        elif user.is_admin:
            admin.user_set.add(user)
            print("Add to admin")
        else:
            worker.user_set.add(user)
            print("Add to workers")

    def _create_user(self, username, email, password, **extra_fields):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(
            email),  **extra_fields)
        user.set_password(password)
        user.save()

        self.add_to_group(user)

        return user

    def create_user(self, username, email, password=None):
        return self._create_user(username, email, password=password)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, email,
                                 password=password,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_root_admin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=3)
        token = jwt.encode({
            'id': self.id,
            'exp': int(time.mktime(dt.timetuple()))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token


class Task(models.Model):
    STATUS = (
        ('ON HOLD', 'ON HOLD'),
        ('PROCESS', 'PROCESS'),
        ('DONE', 'DONE')
    )
    title = models.CharField(max_length=256, unique=True)
    descriptions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=256, choices=STATUS)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title


class Project(models.Model):
    permission_classes = [IsAuthenticated]
    STATUS = (
        ('ACTIVE', 'ACTIVE'),
        ('FINISHED', 'FINISHED')
    )
    name = models.CharField(max_length=256, unique=True)
    descriptions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=256, choices=STATUS)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
