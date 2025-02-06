from django.contrib import admin
from django.contrib.sites.models import Site
from .models import event,organizer
# Register your models here.
admin.site.register(event)
admin.site.register(organizer)