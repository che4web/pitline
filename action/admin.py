from django.contrib import admin
from action.models import Action
# Register your models here.
@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    pass
