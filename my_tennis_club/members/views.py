from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def members_view(request):
    return HttpResponse("Hello world!")