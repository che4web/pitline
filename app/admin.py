#! -*- coding=utf-8 -*-
from django.contrib import admin
from app.models import Feedback, Project, Director, MainText,TextCategory

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectkAdmin(admin.ModelAdmin):
    pass

@admin.register(Director)
class ProjectkAdmin(admin.ModelAdmin):
    pass
@admin.register(MainText)
class MainTextAdmin(admin.ModelAdmin):
    list_display = ('name','text', 'category',)
    list_filter = ('category',)
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('name','slug')
        return self.readonly_fields

@admin.register(TextCategory)
class TextCategoryAdmin(admin.ModelAdmin):
    pass
