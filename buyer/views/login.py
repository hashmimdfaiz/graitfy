from django.shortcuts import render, HttpResponse, redirect
from django.views import View

# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,'buyer/login.html')
    def post(self,request):
        return render(request,'buyer/login.html')
class Otp(View):
    def get(self,request):
        return render(request,'buyer/otp.html')
    def post(self,request):
        return render(request,'buyer/otp.html')

class Logout(View):
    def get(self,request):
        return redirect('buyer_homepage')
    # def post(self,request):
    #     return render(request,'buyer/otp.html')