from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import UserForm, TaskForm, CommentForm
from .models import User, Comment, Task


def projects(request):

    users = User.objects.all()
    tasks = Task.objects.all()
    return render(request, 'Projects/projects.html',{"users": users, 'tasks': tasks})


def project(request, pk):
    return render(request, 'Projects/single-project.html')


def createUser(request):
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'Projects/user_form.html', context)


def updateUser(request, pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'Projects/user_form.html', context)


def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('projects')


def createTask(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'Projects/task_form.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'Projects/task_form.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('projects')


def createComment(request):
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'Projects/comment_form.html', context)