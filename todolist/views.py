from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Todo

# Create your views here.

def list(request):
    # if request.method=="POST": 
    #     title=request.get('title')
    #     description=request.get('description')
    #     is_active=request.get('is_active')
    #     if not is_active:
    #         is_active==False
    #     elements=Todo(title=title,description=description, is_active=is_active)
    #     elements.save()
    obj=Todo.objects.all()
    context={'list':obj}
    return render(request,'list.html', context)
def add(request):
    if request.method=="POST":
        title=request.POST.get('title')
        if not title:
            return redirect('list')
        description=request.POST.get('description')
        is_active=request.POST.get('is_active')
        if is_active=='on':
            is_active=True
        if is_active=='off':
            is_active=False
        if is_active=='unknown':
            is_active=False
        print(is_active)
        elements=Todo(title=title,description=description,is_active=is_active)
        elements.save()
        return redirect('list')
    return render(request,'add.html')

def delete(request, id):
    item=Todo.objects.get(id=id)
    print(item)
    try:
        item.delete()
        return redirect('list')
    except:
        return render(request,'list.html')
def active(request, id):
    item=Todo.objects.get(id=id)
    print(item.is_active)
    if item.is_active==True:
        item.is_active=False
        item.save()
        return redirect('list')
    if not item.is_active==True:
        item.is_active=True
        item.save()
        return redirect('list')
    return render(request,'active.html')