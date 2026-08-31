from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']
    list_filter = ['date', 'email']
    search_fields = ['email']
    date_hierarchy = 'date'
    ordering = ['date', 'email']
