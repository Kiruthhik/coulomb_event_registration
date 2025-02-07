from django.contrib import admin
from django.contrib.sites.models import Site
from .models import event,organizer,Participant,teammate
# Register your models here.
admin.site.register(event)
admin.site.register(organizer)
admin.site.register(Participant)
admin.site.register(teammate)