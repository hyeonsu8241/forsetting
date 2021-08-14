from django.urls import path

from todoapp import views
from todoapp.views import TodoListView, TodoCreateView

app_name = 'todoapp'

urlpatterns = [
    path('list/', TodoListView.as_view(), name='list'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.todo_update, name='update'),
    path('delete/<int:pk>', views.todo_delete, name='delete'),
    path('check/<int:pk>', views.todo_check, name='check'),
    path('delete_all/', views.todo_delete_all, name='delete_all'),
]