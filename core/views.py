from django.shortcuts import render, get_object_or_404
from base.models import *

def home(request):
    portfolio = Portfolio.objects.all()
    blog = Blog.objects.all()
    context = {'portfolio': portfolio,'blog': blog}
    return render(request, 'index.html', context=context)