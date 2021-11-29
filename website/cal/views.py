from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import calendar
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import *
from .utils import Calendar
from .forms import EventForm
from django.contrib import messages

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request):
    form = EventForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            Event.objects.create(
                title = request.POST.get('title'),
                meetid = request.POST.get('meetid'),
                participant = User.objects.get(id=request.POST['participant']),
                start_time = request.POST.get('start_time'),
                end_time = request.POST.get('end_time'),
                materials = request.POST.get('materials'))
            messages.success(request, f'Your Event was added. You will be notified 30 minutes prior to the event start time at the e-mail address on file.')
            return redirect('calendar')
    return render(request, 'cal/event.html', {'form': form})

class EventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'meetid', 'participant', 'start_time', 'end_time', 'materials']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.participant:
            return True
        return False