from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"myapp/index.html")

def login(request):
    return render(request,"myapp/login.html")

def signup(request):
    return render(request,"myapp/signup.html")