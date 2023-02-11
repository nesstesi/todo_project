from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from tasks.models import Task

@login_required
def index(request):
    user = request.user
    context = {
        'tasks': user.task_set.all()
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
