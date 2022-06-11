from django.shortcuts import render
from django.http import HttpResponse


def databaseManagement(request):
    return render(request, "DBadministrator/databaseManagement.html")