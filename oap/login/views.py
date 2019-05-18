from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

def index(request):
    return render(request, 'login/index.html')
def register(request):
    return render(request, 'login/register.html')
    if request.method =="POST":
        user_name = request.POST.get('user_name','')
        password = request.POST.get('password','')
        customer = Customer(user_name = user_name, password = password)
        customer.save()
    