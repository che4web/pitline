from django.contrib import admin
from app.models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass
