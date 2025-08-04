from django.urls import path
from task_management import views

app_name = 'task_management'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
