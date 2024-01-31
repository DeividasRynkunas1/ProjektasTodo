from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from.models import user
#from.models import Uzrasai
#from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from.models import Uzrasai
from django.views import generic
from django.contrib.auth.models import User


class landingpageview(generic.TemplateView):
    template_name = 'home.html'
class UzduotisListView(generic.ListView):
    model = Uzrasai
    template_name = 'uzrasai.html'
    context_object_name = 'uzrasai'


