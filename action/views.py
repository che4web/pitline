from django.shortcuts import render
from action.models import Action
from django.views.generic import ListView
# Create your views here.
class ActionListView(ListView):
    model =Action