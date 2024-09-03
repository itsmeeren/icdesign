from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Event, EventImage

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1  # Number of empty forms to display

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_done')
    list_filter = ('is_done',)
    search_fields = ('title', 'description')
    inlines = [EventImageInline]

admin.site.register(Event, EventAdmin)


