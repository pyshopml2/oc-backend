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
    path('client/', include(client_router.urls)),
    path('document/', include(document_router.urls)),
    path('position/', include(position_router.urls)),
    path('user/', include(user_router.urls)),
    path('employee/', include(employee_router.urls)),
    path('person/', include(person_router.urls)),
    path('storage/', include(storage_router.urls)),
    path('task/', include(task_router.urls)),
]
