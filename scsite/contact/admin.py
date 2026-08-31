from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date']
    list_filter = ['date', 'email', 'name']
    search_fields = ['name', 'email', 'message']
    date_hierarchy = 'date'
    ordering = ['date', 'name']
