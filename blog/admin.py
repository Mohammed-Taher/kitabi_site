from django.contrib import admin
from .models import *

class commentInline(admin.StackedInline):
    model = comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'pub_date', 'comments_number')
    list_filter = ['pub_date']
    inlines = [commentInline]


class commentAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'email' , 'accepted')


class postsInline(admin.StackedInline):
    model = post
    extra = 1

class categoryAdmin(admin.ModelAdmin):
    inlines = [postsInline]


admin.site.register(post, PostAdmin)
admin.site.register(author)
admin.site.register(category, categoryAdmin)
admin.site.register(comment, commentAdmin)
