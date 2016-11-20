from django.contrib import admin
from app.models import Feedback, Project

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectkAdmin(admin.ModelAdmin):
    pass
