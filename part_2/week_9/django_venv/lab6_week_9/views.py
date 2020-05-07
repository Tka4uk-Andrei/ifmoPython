from django.shortcuts import render
from django.http import HttpResponse
from .models import get_list
# Create your views here.

def index(request):

    return HttpResponse(get_list())
