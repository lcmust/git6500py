from django.contrib import admin
from blog.models import Blog, Author, Tag

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'author', 'publish_time')
    fields = ['caption', 'author', 'tags', 'content']
    list_filter = ['publish_time']
    search_fields = ['caption']
    date_hierarchy = 'publish_time'

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
#admin.site.register(Blog)
admin.site.register(Tag)