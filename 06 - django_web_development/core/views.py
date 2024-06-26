from core.models import Event
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime
from datetime import timedelta
from django.http.response import Http404
from django.http.response import JsonResponse

# Create your views here.


# def index(request):
#     return redirect('/schedule/')


def login_user(request):
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/")


def submit_login(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
    return redirect("/")


@login_required(login_url="/login/")
def events_list(request):
    user = request.user
    current_date = datetime.now() - timedelta(hours=1)
    user_event = Event.objects.filter(user=user, event_date__gt=current_date)
    data = {"events": user_event}
    return render(request, "schedule.html", data)


@login_required(login_url="/login/")
def event(request):
    event_id = request.GET.get("id")
    data = {}
    if event_id:
        data["event"] = Event.objects.get(id=event_id)
    return render(request, "event.html", data)


@login_required(login_url="/login/")
def submit_event(request):
    if request.POST:
        title = request.POST.get("title")
        event_date = request.POST.get("event_date")
        description = request.POST.get("description")
        user = request.user
        event_id = request.POST.get("event_id")
        if event_id:
            user_event = Event.objects.get(id=event_id)
            if user_event.user == user:
                user_event.title = title
                user_event.description = description
                user_event.event_date = event_date
                user_event.save()
            # Event.objects.filter(id=event_id).update(title=title, event_date=event_date,
            #                                          description=description)
        else:
            Event.objects.create(
                title=title, event_date=event_date, description=description, user=user
            )
    return redirect("/")


@login_required(login_url="/login/")
def delete_event(request, event_id):
    user = request.user
    try:
        user_event = Event.objects.get(id=event_id)
    except Exception:
        raise Http404()
    if user == user_event.user:
        user_event.delete()
    else:
        raise Http404()
    return redirect("/")


def json_events_list(request, user_id):
    user = User.objects.get(id=user_id)
    user_event = Event.objects.filter(user=user).values('id', 'title')
    return JsonResponse(list(user_event), safe=False)
