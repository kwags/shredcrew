from django import template
from ..models import Event
register = template.Library()

@register.simple_tag
def total_events():
    return Event.published.count()

@register.inclusion_tag('events/event/latest_events.html')
def show_latest_events(count=5):
    latest_events = Event.published.order_by('date')[:count]
    return {'latest_events': latest_events}

@register.inclusion_tag('events/event/events_slider.html')
def show_events_slider(count=9):
    events_slider = Event.published.order_by('date')[:count]
    return {'events_slider': events_slider}

