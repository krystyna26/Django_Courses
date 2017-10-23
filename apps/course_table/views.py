from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import Course

def index(request):
    allCreatedCourses = {
        "allCourses" : Course.objects.all()
    }
    return render(request, "course_table/index.html", allCreatedCourses)



def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/')
    else:
        Course.objects.create(
            courseName = request.POST['courseName'],
            description = request.POST['description'] 
        )
    return redirect('/')



def areyousure(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, 'course_table/destroy.html', context)



def destroy(request, id):
    dest = Course.objects.get(id=id)
    dest.delete()
    return redirect('/')