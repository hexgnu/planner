from django.shortcuts import render, redirect

from lessons.models import Lesson

from .models import Practice, HomeworkItemTimer
from .forms import FinishPracticeForm

def index(request):
    # TODO fix this...
    last_lesson = Lesson.objects.order_by('-scheduled_at').first()

    practice, is_new = Practice.objects.get_or_create(finished=False, lesson=last_lesson)

    form = FinishPracticeForm()
    return render(request, 'practices/index.html', {'homework_item_timers': practice.plan(), 'lesson': last_lesson, 'practice': practice, 'form': form})

def finish(request, id=None):
    id = request.POST['id']

    practice = Practice.objects.get(pk=id)
    practice.finished = True
    practice.save()

    return redirect('/practices')

def create_timer(request):
    print(request.POST)

    hit = HomeworkItemTimer.objects.get(pk=request.POST['id'])

    hit.seconds = request.POST['seconds']

    hit.save()

    return redirect('/practices')
