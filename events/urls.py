from django.urls import path

from .views import (EventsListView, EventCreateView, EventEditView,
                    EventDeleteView, CategoryCreateView, EventsCalendarView,
                    EventApproveView)

app_name = "events"

urlpatterns = [
    path('', EventsListView.as_view(), name="events_list"),
    path('calendar', EventsCalendarView.as_view(), name="events_calendar"),
    path('create', EventCreateView.as_view(), name="event_create"),
    path('edit/<int:event_id>', EventEditView.as_view(), name="event_edit"),
    path('approve/<int:event_id>', EventApproveView.as_view(), name="event_approve"),
    path('delete/<int:event_id>', EventDeleteView.as_view(), name="event_delete"),
    path('category/create', CategoryCreateView.as_view(), name="category_create")
]
