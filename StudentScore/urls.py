from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowStudentDetail, name="ShowChart"),
]
