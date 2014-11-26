# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class PollAdmin(admin.ModelAdmin):
   fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
   inlines = [ChoiceInline]
   #Customize the admin change list
   list_display = ('question', 'pub_date')
   list_display = ('question', 'pub_date', 'was_published_recently')
   
   #添加列表过滤
   list_filter = ['pub_date']
   
   #添加查询
   search_fields = ['question']
   
admin.site.register(Poll, PollAdmin)
