from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from tasks.models import Task

def index(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'tasks/tasks.html', context=context)
    # return render(request, 'tasks/base.html', context=context)

def detail(request, task_id):
    # task = Task.objects.get(id=task_id)
# return HttpResponse("You're looking at task %s." % task_id)
    # return render(request, 'tasks/details')
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'tasks/detail.html', {'task': task})
