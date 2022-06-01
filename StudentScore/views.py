from django.shortcuts import render
from .models import Student
from .utils import get_plot

# Create your views here.

def ShowStudentDetail(request):
    qs = Student.objects.all()
    x = [x.name for x in qs]
    y = [y.score for y in qs]
    chart = get_plot(x, y)
    return render(request, 'index.html', {'chart': chart})
