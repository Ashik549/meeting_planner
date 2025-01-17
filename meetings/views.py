from django.shortcuts import render, get_object_or_404, redirect

from .models import Meeting, Room
from .forms import MeetingForm

# Create your views here.

def detail(request, id):
    meeting_detail = get_object_or_404(Meeting, pk = id)
    return render(request, "meetings/detail.html", {"meeting": meeting_detail})


def rooms(request):
    return render(request, "meetings/rooms.html", {"rooms": Room.objects.all()})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = MeetingForm()

    return render(request, "meetings/new.html", {"form": form})