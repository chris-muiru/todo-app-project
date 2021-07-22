from django.shortcuts import render,redirect
from .forms import user_form
from .models import user_data

def index(request):
    todo_list=user_data.objects.order_by('-start_date')
    database_temp=user_data.objects.all()
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            task=form.cleaned_data["task"]
            start=form.cleaned_data["start"]
            finish=form.cleaned_data["finish"]
            database=user_data(task_name=task,start_date=start,finish_date=finish)
            database.save()
            
    else:
        form=user_form()
    
    context={"form":form,
             "list":todo_list
             }
    return render(request,"todo_app/index.html",context)

def remove(request,user_item):
    item=user_data.objects.get(pk=user_item)
    item.delete()
    return redirect('index_page')


# def update(request,pk):



# Create your views here