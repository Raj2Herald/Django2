from django.http import HttpResponse
from django.shortcuts import render

def hello_world_view(request):
    return HttpResponse("<h1>Hello world<h1>")

def hello_world_from_htmlpage(request):
    return render(request,'index.html',{'name':'Ram'})

def form_view(request):
    return render(request,'form.html')

def form_data(request):
    formdata = request.GET['personname']
    print(formdata)
    return render(request,'form.html',{'personnamekey':formdata})
