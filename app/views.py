"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from app.forms import ContactForm
from django.views.generic.edit import FormView

from django.shortcuts import HttpResponse
import json
from django.http import HttpResponseBadRequest
from app.models import Feedback, Project, Director,MainText,TextCategory
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'feedback_list':Feedback.objects.filter(active=True),
            'projects':Project.objects.filter(active=True),
            'year':datetime.now().year,
            'form_foto':ContactForm(),
            'text_title':MainText.objects.filter(category_id=1),
            'text_reasons':TextCategory.objects.get(pk=2),
            'description':MainText.objects.get(slug='descriptionMain').text,
            'keywords':MainText.objects.get(slug='keywordsMain').text,
            'title':MainText.objects.get(slug='MainTitle').text,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return HttpResponse('{"data": "OK"}')

    def form_invalid(self, form):
        errors_dict = json.dumps(dict([(k, [e for e in v]) for k, v in form.errors.items()]))
        #error_list=[]
        #for k, v in form.errors.items():
        #    for e in v:
        #        error_list.append(e)
        #errors_dict =','.join(error_list)
        return HttpResponseBadRequest(errors_dict)

def director(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/director.html',
        {
            'title':'Contact',
            'object':Director.objects.get(id=1),
        }
    )

