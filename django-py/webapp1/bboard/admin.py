from django.contrib import admin
from .models import Bb, Rubric

class BbAdmin(admin.ModelAdmin):
    list_diplay = ('title', 'content', 'price', 'published', 'rubric')
    list_diplay_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
