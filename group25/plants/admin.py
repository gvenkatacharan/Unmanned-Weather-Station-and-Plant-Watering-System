# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Temperature,Humidity,Plant,Waterlevel,Watersensor,Plantcondition

admin.site.register(Plant)
admin.site.register(Plantcondition)
admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Waterlevel)
admin.site.register(Watersensor)