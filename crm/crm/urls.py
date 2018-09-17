from django.contrib import admin
from django.urls import path, include, re_path
from api.v1.document.routes import document_router
from api.v1.client.routes import client_router
from api.v1.user.routes import user_router
from api.v1.employee.routes import employee_router
from api.v1.position.routes import position_router
from api.v1.person.routes import person_router
from api.v1.storage.routes import storage_router
from api.v1.temp_token.views import temporary_auth_token
from api.v1.task.routes import task_router
from api.v1.personal_account.views import personal_account
from rest_framework.authtoken import views

from api.v1.auth.view import obtain_auth_token, reset_password

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
    path('account', personal_account, name='account'),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('token/', obtain_auth_token, name='token'),
    path('reset-password/', reset_password, name='reset-password'),

    path('client/', include(
        (client_router.urls, 'client_app'), namespace='client')),

    path('document/', include(
        (document_router.urls, 'document_app'), namespace='document')),

    path('position/', include(
        (position_router.urls, 'position_app'), namespace='position')),

    path('employee/', include(
        (employee_router.urls, 'employee_app'), namespace='employee')),

    path('person/', include(
        (person_router.urls, 'person_app'), namespace='person')),

    path('storage/', include(
        (storage_router.urls, 'storage_app'), namespace='storage')),

    path('task/', include(
        (task_router.urls, 'task_app'), namespace='task')),

    path('user/', include(
        (user_router.urls, 'user_app'), namespace='user')),

    path('temp-token/<str:token>/', temporary_auth_token, name='temp_token')
]
