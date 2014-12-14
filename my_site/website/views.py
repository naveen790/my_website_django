from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    context = RequestContext(request)
    
    return render_to_response('website/index.html',context)

def contact(request):
    context = RequestContext(request)
    
    return render_to_response('website/contact.html',context)

def resume(request):
    context = RequestContext(request)
    
    return render_to_response('website/resume.html',context)

def courses(request):
    context = RequestContext(request)
    
    return render_to_response('website/courses.html',context)

