from django.shortcuts import render,get_object_or_404,redirect
from .models import Project
from django.views.generic import CreateView
from .forms import *



def project_list(request):
    return render(request,'budget/project-list.html')

def project_detail(request,project_slug):
    project=get_object_or_404(Project,slug=project_slug)
    expense_list=project.expenses.all()
    form=ExpenseForm
    # form is now showing up
    return render(request,'budget/project-detail.html',{'project':project,'expense_list':expense_list , 'form':form})

class ProjectCreateView(CreateView):
    model=Project
    template_name='budget/add-project.html'
    fields=('name','budget')



