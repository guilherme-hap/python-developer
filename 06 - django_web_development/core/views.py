from django.shortcuts import render
from core.models import Event

# Create your views here.


# def index(request):
#     return redirect('/schedule/')


def events_list(request):
    event = Event.objects.all()
    data = {'events': event}
    return render(request, 'schedule.html', data)
