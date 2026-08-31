from django.shortcuts import render, get_object_or_404
from .models import Event
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from taggit.models import Tag


def event_list(request, tag_slug=None):
    event_list = Event.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        event_list = event_list.filter(tags__in=[tag])
    # Pagination with 3 posts per page
    paginator = Paginator(event_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        events = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        events = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        events = paginator.page(paginator.num_pages)
    return render(request,
                  'events/event/list.html',
                  {'events': events,
                   'tag': tag})


def event_detail(request, year, month, day, event):
    event = get_object_or_404(Event,
                              status=Event.Status.PUBLISHED,
                              slug=event,
                              date__year=year,
                              date__month=month,
                              date__day=day)
    # List of similar posts
    event_tags_ids = event.tags.values_list('id', flat=True)
    similar_events = Event.published.filter(tags__in=event_tags_ids) \
        .exclude(id=event.id)
    similar_events = similar_events.annotate(same_tags=Count('tags')) \
                        .order_by('-same_tags', 'date')[:3]
    return render(request,
                  'events/event/detail.html',
                  {'event': event,
                   'similar_events': similar_events})
