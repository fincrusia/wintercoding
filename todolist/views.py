from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo
from django.utils.timezone import datetime

# Create your views here.


def index(request):

    invalid_form = False
    modify_mode = False
    modify_pk = -1
    todos = Todo.objects.all()

    if(request.method == "POST"):
        if(request.POST.get("add",False)):
            try:
                newTodo = Todo()
                newTodo.title = request.POST["title"]
                newTodo.content = request.POST["content"]
                newTodo.priority = request.POST["priority"]
                newTodo.due = request.POST["due"]

                newTodo.save()

            except:
                invalid_form = True
    
        elif(request.POST.get("remove",False)):
            for todo in todos:
                if request.POST.get("todo"+str(todo.pk),False):
                    todo.delete()

        elif(request.POST.get("done",False)):
            for todo in todos:
                if request.POST.get("todo"+str(todo.pk),False):
                    todo.done = True
                    todo.save()

        else:
            for todo in todos:
                if request.POST.get("modify"+str(todo.pk),False):
                    modify_mode = True
                    modify_pk = todo.pk
                
                if request.POST.get("modifyas"+str(todo.pk),False):
                    target = Todo.objects.filter(pk=todo.pk)[0]
                    if(request.POST.get("title2",False)):
                        target.title = request.POST["title2"]
                    if(request.POST.get("content2",False)):
                        target.content = request.POST["content2"]
                    if(request.POST.get("priority2",False)):
                        target.priority = request.POST["priority2"]
                    target.save()


    todos = Todo.objects.all()
    #now = datetime.now()
    #expired = Todo.objects.filter(due__lte = now, done = False)
    template = loader.get_template("todolist.html")
    context = {
        #"now" : now,
        "todos" : todos,
        #"expired" : expired,
        "invalid_form" : invalid_form,
        "modify_mode" : modify_mode,
        "modify_pk" : modify_pk,
    }
    return HttpResponse(template.render(context,request))