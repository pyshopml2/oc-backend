"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from api.v1.document.routes import document_router
from api.v1.client.routes import client_router
from api.v1.user.routes import user_router
from api.v1.employee.routes import employee_router
from api.v1.position.routes import position_router
from api.v1.person.routes import person_router
from api.v1.storage.routes import storage_router
from api.v1.task.routes import task_router
from rest_framework.authtoken import views

from api.v1.auth.view import obtain_auth_token
from api.v1.task.viewsets import OwnTasks

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('own/', OwnTasks.as_view(), name='own_tasks'),
    path('token/', obtain_auth_token, name='token'),

    path('client/', include(
        (client_router.urls, 'client_app'), namespace='client')),

    path('document/', include(
        (document_router.urls, 'document_app'), namespace='document')),

    path('position/', include(
        (position_router.urls, 'position_app'), namespace='position')),

    path('user/', include(
        (user_router.urls, 'user_app'), namespace='user')),

    path('employee/', include(
        (employee_router.urls, 'employee_app'), namespace='employee')),

    path('person/', include(
        (person_router.urls, 'person_app'), namespace='person')),

    path('storage/', include(
        (storage_router.urls, 'storage_app'), namespace='storage')),

    path('task/', include(
        (task_router.urls, 'task_app'), namespace='task')),
]
