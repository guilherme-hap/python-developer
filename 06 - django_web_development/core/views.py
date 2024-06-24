from core.models import Event
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.


# def index(request):
#     return redirect('/schedule/')


def login_user(request):
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
    return redirect("/")


@login_required(login_url="/login/")
def events_list(request):
    user = request.user
    user_event = Event.objects.filter(user=user)
    data = {"events": user_event}
    return render(request, "schedule.html", data)


@login_required(login_url='/login/')
def event(request):
    return render(request, 'event.html')


@login_required(login_url='/login/')
def submit_event(request):
    if request.POST:
        title = request.POST.get('title')
        event_date = request.POST.get('event_date')
        description = request.POST.get('description')
        user = request.user
        Event.objects.create(title=title, event_date=event_date,
                             description=description, user=user)
    return redirect('/')
