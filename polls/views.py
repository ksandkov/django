from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('test')

def detail(request, question_id):
    return HttpResponse("You're looking at question {}".format(question_id))

def results(request, question_id):
    return HttpResponse("You're looking at results of question {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
