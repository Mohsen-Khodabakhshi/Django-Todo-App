from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import ToDo
from .forms import NewToDoForm

from django.http import HttpResponse

# Create your views here.
class NotDoneList(ListView):
    context_object_name = "NotDone"
    template_name = "todo/notDone.html"
    paginate_by = 5

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user, status="Not Done")

class DoneList(ListView):
    context_object_name = "Done"
    template_name = "todo/done.html"
    paginate_by = 5

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user, status="Done")

def newToDo(request):
    if request.method == 'POST':
        form = NewToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.title = form.cleaned_data.get('title')
            todo.descrtption = form.cleaned_data.get('descrtption')
            todo.due_on = request.POST.get('due_on')
            todo.color = request.POST.get('color')
            todo.user = request.user
            todo.save()
            return redirect('/nd')
    else:
        form = NewToDoForm()
        context = {'form': form}
        return render(request, 'todo/new.html', context)

def delete(request):
    previous_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        user = request.user
        id = request.POST.get('id-delete')
        query = ToDo.objects.get(id=id)
        if user == query.user:
            query.delete()
            return redirect(previous_url)
    else:
        return redirect(previous_url)

def ToDoDetail(request, slug):
    queryset = get_object_or_404(ToDo, id=slug)
    context = {
        'todo' : queryset
    }
    return render(request, 'todo/detail.html', context)

def statusToDo(request):
    previous_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        id = request.POST.get('id-status')
        queryset = ToDo.objects.get(id=id)
        if queryset.status == "Not Done":
            queryset.status = "Done"
            queryset.save()
            return redirect(previous_url)
        if queryset.status == "Done":
            queryset.status = "Not Done"
            queryset.save()
            return redirect(previous_url)
    else:
        return redirect(previous_url)