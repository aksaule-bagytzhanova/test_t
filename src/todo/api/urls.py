from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename="tasks")
router.register(r'organizations', views.OrganizationViewSet, basename="organizations")
router.register(r'projects', views.ProjectViewSet, basename="projects")


urlpatterns = [
    path('', include(router.urls)),
    path('users/register/', views.RegistrationAPIView.as_view()),
    path('users/login/', obtain_auth_token, name='api_token_auth'),
]
