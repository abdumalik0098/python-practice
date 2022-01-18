from django import template
from django.http import HttpRequest, request
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Bb

def index(request):
   # template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
   # context = {'bbs':bbs}
   # return HttpResponse(template.render(context, request))
    return render(request, 'bboard/index.html', {'bbs': bbs})
