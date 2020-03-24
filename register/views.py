from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, CreateView

from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "register/employee_form.html", {'form' : form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST, request.FILES)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, request.FILES, instance=employee)

        if form.is_valid():
            form.save()

        return redirect('employee_list')

class EmployeeList(ListView):
    model = Employee
    template_name = 'register/employee_list.html'
    context_object_name = 'employee_list'

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'register/employee_detail.html'
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Employee, id=id_)

def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')
