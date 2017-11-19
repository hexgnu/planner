from django.shortcuts import render
from django.http import HttpResponse
from .models import Lesson, HomeworkItem
import random
import django
import datetime

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter


def index(request):
    last_10_lessons = Lesson.objects.order_by('-scheduled_at')[:10]
    items = last_10_lessons.first().homework_items.all()
    return render(request, 'lessons/index.html', {'lessons': last_10_lessons, 'homework_items': items})

# Lesson is edited by teacher
def teacher_edit(request):
    return render(request, 'teacher_edit.html', {'lesson': Lesson})
    
# Lesson is edited by student
def student_edit(request):
    return render(request, 'student_edit.html', {'lesson': Lesson})

def progress_png(request):
    lessons = Lesson.objects.order_by('-scheduled_at').all()

    rows = []
    
    x=[]
    y=[]
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


# Create your views here.
