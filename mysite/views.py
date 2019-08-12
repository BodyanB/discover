from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from mysite.models import Profi
def hello(request):
    return  render(request ,"index.html")

def instructors_list(request):
    instructors = Profi.objects.all()
    return  render(request ,"instructors.html", {"instructors_list" : instructors })

def hello_python(request, some):
    return  HttpResponse("Hello Python." + some )

def http (request):

    response = render (request , "http.html" )
    print(response ['Content-Type'])
    response['Age'] = 2000
    response.status_code = 404
    return HttpResponseNotFound('404')

def sum_two (request, a, b):
    s = int(a) + int(b)
    print(a,b)
    return HttpResponse(s)

