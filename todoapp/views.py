from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import FormMixin, CreateView

from todoapp.forms import TodoCreationForm
from todoapp.models import Todo


@method_decorator(login_required(login_url='/accounts/login/'), 'get')
class TodoListView(ListView, FormMixin):
    model = Todo
    form_class = TodoCreationForm
    context_object_name = 'todo_list'
    template_name = 'todoapp/list.html'

    def get_context_data(self, **kwargs):
        object_list = Todo.objects.filter(user=self.request.user).order_by('done')
        return super(TodoListView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(login_required(login_url='/accounts/login/'), 'get')
@method_decorator(login_required(login_url='/accounts/login/'), 'post')
class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoCreationForm
    template_name = 'todoapp/create.html'

    def form_valid(self, form):
        temp_todo = form.save(commit=False)
        temp_todo.user = self.request.user
        temp_todo.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todoapp:list')


@login_required(login_url='/accounts/login/')
def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.user == request.user:
        todo.delete()
        return HttpResponseRedirect(reverse('todoapp:list'))


@login_required(login_url='/accounts/login/')
def todo_delete_all(request):
    todo_list = Todo.objects.filter(user=request.user)
    for todo in todo_list:
        todo.delete()
    return HttpResponseRedirect(reverse('todoapp:list'))


@login_required(login_url='/accounts/login/')
def todo_update(request, pk):
    content = request.POST.get('title')
    todo = Todo.objects.get(pk=pk)
    user = request.user

    todo.content = content
    todo.user = user
    todo.save()

    return HttpResponseRedirect(reverse('todoapp:list'))


@login_required(login_url='/accounts/login/')
def todo_check(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.done = not todo.done
    todo.save()

    return HttpResponseRedirect(reverse('todoapp:list'))