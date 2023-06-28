from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
class Cart(View):
    def get(self,request):
        return render(request,'buyer/cart.html')
    def post(self,request):
        return render(request,'buyer/cart.html')
class Place_order(View):
    def get(self,request):
        return render(request,'buyer/place_order.html')
    def post(self,request):
        return render(request,'buyer/place_order.html')
class Payment_order_place(View):
    def get(self,request):
        return render(request,'buyer/payment_place_order.html')
    def post(self,request):
        return render(request,'buyer/payment_place_order.html')
class My_order(View):
    def get(self,request):
        return render(request,'buyer/ordersummary.html')
    def post(self,request):
        return render(request,'buyer/ordersummary.html')