from django.shortcuts import render, HttpResponse,redirect


def root(request):
    return redirect("/blogs")
# Create your views here.


def register(request):              
    return HttpResponse("placeholder for users to create a new user record" ) 


def login(request):
    return HttpResponse("placeholder for users to log in")


def users(request):
    return redirect('/blogs')
    return HttpResponse("placeholder to later display all the list of users")