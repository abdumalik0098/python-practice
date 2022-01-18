from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect

def todoView(request):
    all_todo_item = TodoItem.objects.all()
    return render(request, 'index.html', {'all_item': all_todo_item})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/myapp/')

def deleteItemView(request, i):
    y = TodoItem.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect('/myapp/')