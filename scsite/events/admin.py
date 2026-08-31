from django.contrib import admin

from.models import Event, Location
admin.site.register(Location)

@admin.register(Event)

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location']
    list_filter = ['status', 'date', 'title']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'date']