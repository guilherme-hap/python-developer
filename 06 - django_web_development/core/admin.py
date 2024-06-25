from django.contrib import admin
from .models import Event

# Register your models here.


class AdminEvent(admin.ModelAdmin):
    list_display = ('id', 'title', 'event_date', 'creation_date')
    list_filter = ('title', 'event_date',)


admin.site.register(Event, AdminEvent)
