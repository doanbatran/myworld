from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Thêm Model Member
from .models import Member

# Create your views here.
def members_view(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))