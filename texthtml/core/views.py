from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.


def home(request):
    form = PostText
    return render(request,'text.html',{'form':form})