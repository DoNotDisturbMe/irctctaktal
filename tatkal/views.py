from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, Http404, HttpResponsePermanentRedirect, NoReverseMatch
import datetime
import time
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.core.mail import message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from  django.contrib import messages
from django.urls import reverse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from .models import *
# from .decorator import loginreqired


# Create your views here.

def welcome(request):
    return render(request,'clientbase.html')