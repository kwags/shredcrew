from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    # Event views
    # path('', views.event_list, name='event_list'),
    path('tag/<slug:tag_slug>/',
         views.event_list, name='event_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:event>/',
         views.event_detail,
         name='event_detail'),
]
