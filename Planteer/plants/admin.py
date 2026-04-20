from django.contrib import admin

from .models import Plant, Comment

class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'about','used_for','image', 'category', 'is_edible', 'created_at')
    list_filter = ('category', 'is_edible')

admin.site.register(Plant, PlantAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'plant', 'text', 'created_at')
    list_filter = ('plant', 'created_at')

admin.site.register(Comment, CommentAdmin)
