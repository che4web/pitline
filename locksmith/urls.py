from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from locksmith import views

urlpatterns = [
    url(r'^$', views.home, name='locksmith-index'),
]
