from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
class Cart(View):
    def get(self,request):
        return render(request,'buyer/cart.html')
    def post(self,request):
        return render(request,'buyer/cart.html')