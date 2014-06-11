# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
   fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
admin.site.register(Poll, PollAdmin)
