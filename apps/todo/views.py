import datetime
from http.client import HTTPResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import TodoForm
from .models import Todo

@login_required(login_url="login")
def index(request):
    userID = request.user.pk
    context = {
        "items": Todo.objects.filter(userID=userID).order_by('deadline'),
        "userID": userID
    }
    return render(request, "todo/index.html", context)


@login_required(login_url="login")
def create_view(request):
    # dictionary for initial data with
    # field names as keys

 
    # add the dictionary during initialization
    form = TodoForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.userID = request.user.id
        item.date = datetime.datetime.today().strftime('%Y-%m-%d')
        item.save()
        return redirect('index')
         
    context ={
        "form": form
    }    
    return render(request, "todo/create_view.html", context)

def delete_view(request, pk):
    item = Todo.objects.get(id=pk)
    item.delete()
    return redirect('/')
