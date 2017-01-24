#! -*- coding=utf-8 -*-
from django.contrib import admin
from app.models import Feedback, Project, Director, MainText

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
    pass
