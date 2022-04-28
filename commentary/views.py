from django.shortcuts import render
from django.http import HttpResponse
from . import fetching as ft
# Create your views here.
def index(request):
    return render(request,'index.html')
def create(request):
    if request.method=="POST": 
        link=request.POST['link']
        ft.act=True
        ft.conti(link)
        return HttpResponse("Playing")
        
def stop(request):
    if request.method=="POST": 
        # link=request.POST['link']
        ft.act=False
        msg="Paused"
        return HttpResponse(msg)
    return 
