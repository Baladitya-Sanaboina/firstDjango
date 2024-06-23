from django.shortcuts import render, get_object_or_404
from Employee.models import employee
from django.http import HttpResponse
# Create your views here.

def employee_detail(request,pk):
    employees = get_object_or_404(employee,pk=pk)
    context = {
        'employee':employees
    }
    return render(request,'employee.html',context)
    