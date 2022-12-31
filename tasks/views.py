from django.shortcuts import render

# Create your views here.

def all_tasks(request):
    return render(request, 'tasks/tasks.html', {})

def home(request):
    return render(request, 'tasks/index.html', {})

def about(request):
    return render(request, 'tasks/about.html', {})

def contact(request):
    return render(request, 'tasks/contact.html', {})