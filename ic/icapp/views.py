from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone

from .models import Event

# Create your views here.
from django.shortcuts import render
from .models import Event
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'AboutUs.html')
def events_view(request):
    done_events = Event.objects.filter(is_done=True)
    upcoming_events = Event.objects.filter(is_done=False)
    context = {
        'done_events': done_events,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'events.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Event

def event_detail_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    context = {
        'event': event,
    }
    return render(request, 'event_detail.html', context)


