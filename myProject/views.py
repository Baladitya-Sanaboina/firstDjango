from django.shortcuts import render 
from Employee.models import employee


def home(request):
    content = {
        'employees': employee.objects.all()
    }
    return render(request,'index.html',content)

