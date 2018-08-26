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
from django.urls import path, include
from api.v1.document.routes import document_router
from api.v1.client.routes import client_router
from api.v1.user.routes import user_router
from api.v1.employee.routes import employee_router
from api.v1.position.routes import position_router
from api.v1.person.routes import person_router
from api.v1.storage.routes import storage_router
from api.v1.task.routes import task_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include((client_router.urls, 'client_app'), namespace='client')),
    path('document/', include((document_router.urls, 'document_app'), namespace='document')),
    path('position/', include((position_router.urls, 'position_app'), namespace='position')),
    path('user/', include((user_router.urls, 'user_app'), namespace='user')),
    path('employee/', include((employee_router.urls, 'employee_app'), namespace='employee')),
    path('person/', include((person_router.urls, 'person_app'), namespace='person')),
    path('storage/', include((storage_router.urls, 'storage_app'), namespace='storage')),
    path('task/', include((task_router.urls, 'task_app'), namespace='task')),
]
