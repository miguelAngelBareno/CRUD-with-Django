"""businessAdministrator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from DBadministrator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("databaseManagement/", views.databaseManagement, name="databaseManagement"),
    path("registerCompany/", views.registerCompany, name="registerCompany"),
    path("editCompany/<code>", views.editCompany, name='editCompany'),
    path("companyEdit/", views.companyEdit, name='companyEdit'),
    path("deleteCompany/<code>", views.deleteCompany, name='deleteCompany'),
]
