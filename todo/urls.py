from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ToDoDetail, NotDoneList, DoneList, newToDo, delete, statusToDo

app_name = 'todo'
urlpatterns = [
    path('detail/<int:slug>/', login_required(ToDoDetail), name='detail'),
    path('nd/', login_required(NotDoneList.as_view()), name='nd'),
    path('dn/', login_required(DoneList.as_view()), name='dn'),
    path('new/', login_required(newToDo), name='new'),
    path('delete/', login_required(delete), name='delete'),
    path('status/', login_required(statusToDo), name='status'),
]