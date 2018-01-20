from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator

from .forms import CategoryForm, EventForm
from .models import Category, Event
from .helpers import is_admin, admin_route


class EventsListView(View):
    def get(self, request):
        events = Event.objects.filter(start__gte=datetime.now()).order_by('start')
        return render(request, 'events_list.html', {
            'events': events,
            'is_admin': is_admin(request)
        })


@method_decorator(admin_route, name='dispatch')
class EventCreateView(View):
    def get(self, request):
        form = EventForm()
        form.helper.form_method = 'post'
        form.helper.form_action = reverse('events:event_create')
        return render(request, 'event.html', {'form': form})

    def post(self, request):
        form = EventForm(request.POST, request.FILES)

        try:
            form.save()
        except ValueError as e:
            return render(request, 'event.html', {'form': form})

        return redirect('events:events_list')


@method_decorator(admin_route, name='dispatch')
class EventEditView(View):
    def get(self, request, event_id):

        try:
            event = Event.objects.get(pk=event_id)
        except:
            return redirect('events:events_list')

        form = EventForm(instance=event)
        form.helper.form_method = 'post'
        form.helper.form_action = reverse('events:event_edit', kwargs={
            'event_id': event_id
        })
        return render(request, 'event.html', {'form': form})

    def post(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except:
            return redirect('events:events_list')

        form = EventForm(request.POST, request.FILES, instance=event)
        try:
            form.save()
        except ValueError as e:
            return render(request, 'event.html', {'form': form})

        return redirect('events:events_list')


@method_decorator(admin_route, name='dispatch')
class EventDeleteView(View):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except:
            return redirect('events:events_list')

        return render(request, 'event_delete.html', {'event': event})

    def post(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
            event.delete()
        except:
            return redirect('events:events_list')

        return redirect('events:events_list')


@method_decorator(admin_route, name='dispatch')
class CategoryCreateView(View):
    def get(self, request):
        form = CategoryForm()
        form.helper.form_method = 'post'
        form.helper.form_action = reverse('events:category_create')
        return render(request, 'event.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        try:
            form.save()
        except ValueError as e:
            return render(request, 'event.html', {'form': form})

        return redirect('events:events_list')
        