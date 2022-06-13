from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Business


def databaseManagement(request):
    listBusiness = Business.objects.all() #list of companies
    return render(request, "DBadministrator/databaseManagement.html", {"bussines":listBusiness})


def registerCompany(request):
    name = request.POST['txtCompanyName']
    direct = request.POST['txtDirection']
    nitNumber = request.POST['NumNit']
    celphone = request.POST['celphone']

    company = Business.objects.create(company_name=name, direction=direct, NIT=nitNumber, phone=celphone)
    return redirect('/databaseManagement/')


def editCompany(request, code):
    company = Business.objects.get(NIT=code)
    return render(request, "DBadministrator/editCompany.html", {"company":company})

def companyEdit(request):
    name = request.POST['txtCompanyName']
    direct = request.POST['txtDirection']
    nitNumber = request.POST['NumNit']
    celphone = request.POST['celphone']

    company = Business.objects.get(NIT=nitNumber)
    company.company_name = name
    company.direction = direct
    company.phone = celphone

    company.save()
    return redirect('/databaseManagement/')


def deleteCompany(request, code):
    company = Business.objects.get(NIT=code)
    company.delete()
    
    return redirect('/databaseManagement/')