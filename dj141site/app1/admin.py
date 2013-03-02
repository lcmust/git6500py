from app1.models import Poll, Choice
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    """fields = [
        ('Question information',  {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]"""
    #fields = [ 'pub_date', 'question']

class PollAdmin2(admin.ModelAdmin):
    fields = [
        (None, {'fields':['pub_date'], 'class':['collapse']}),
        ('Date information', {'fields':['question'], 'class':['collapse']}),
    ]

admin.site.register(Poll)
# admin.site.register(PollAdmin2)
#admin.site.register(Choice)
