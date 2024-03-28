from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.http import HttpResponseRedirect
from .models import Project
from django.views.generic import CreateView
from .forms import *



def project_list(request):
    return render(request,'budget/project-list.html')

def project_detail(request,project_slug):
    project=get_object_or_404(Project,slug=project_slug)
    expense_list=project.expenses.all()

    if request.method=='GET':
        return render(request,'budget/project-detail.html',{'project':project,'expense_list':expense_list })


    if request.method=='POST':
        form=ExpenseForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            amount=form.cleaned_data['amount']
            category=form.cleaned_data['category']
            project.expenses.objects.create(
                project=project,
                title=title,
                amount=amount,
                category=category
            ).save()  
    return HttpResponseRedirect(project_slug)


def remove_expense(request,id):
    expense=Expense.objects.get(id=id)
    expense.delete()
    return redirect('detail')





class ProjectCreateView(CreateView):
    model=Project
    template_name='budget/add-project.html'
    fields=('name','budget')



