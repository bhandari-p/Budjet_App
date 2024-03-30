from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.http import HttpResponseRedirect
from .models import Project
from django.views.generic import CreateView
from .forms import *



def project_list(request):
    project_list=Project.objects.all()
    return render(request,'budget/project-list.html',{'project_list':project_list})

def project_detail(request,project_slug):
    project=get_object_or_404(Project,slug=project_slug)
    expense_list=project.expenses.all()
    project_list=Project.objects.all()
    form = ExpenseForm(request.POST or None)

    if request.method=='GET':
        return render(request,'budget/project-detail.html',{'project':project,'expense_list':expense_list, 'form':form,'project_list':project_list})


    if request.method=='POST':
        if form.is_valid():
            print(form.cleaned_data)
            title=form.cleaned_data.get("title")
            amount=form.cleaned_data.get("amount")
            category=form.cleaned_data.get("category")
            project.expenses.create(
                title = title,
                amount = amount,
                category = category
            )
    return HttpResponseRedirect(project_slug)


def remove_expense(request,id):
    expense=Expense.objects.get(id=id)
    expense.delete()
    return redirect('detail')





class ProjectCreateView(CreateView):
    model=Project
    template_name='budget/add-project.html'
    fields=('name','budget')



