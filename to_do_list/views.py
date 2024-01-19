from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def index(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task = Task(title=title)
            task.save()
            return redirect('index')
    todos = Task.objects.all() 
    return render(request, 'to_do_list/index.html',{'todos':todos})

def updateTask(request, pk):
    todo = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.save()
        return redirect('index')
    
    return render(request, 'to_do_list/edit.html',{'todo':todo})

def deleteTask(request, pk):
    todo = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')

    return render(request, 'to_do_list/delete.html',{'todo':todo})

def deleteAll(request):
    if request.method == 'POST':
        Task.objects.all().delete()
        return redirect('index')

    return render(request, 'to_do_list/delete_all.html')