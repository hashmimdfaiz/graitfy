from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
class Profile(View):
    def get(self,request):
        return render(request,'buyer/profileupdate.html')
    def post(self,request):
        return render(request,'buyer/profileupdate.html')

class Help(View):
    def get(self,request):
        return render(request,'buyer/help.html')
    def post(self,request):
        return render(request,'buyer/help.html')

class Add_bank_details(View):
    def get(self,request):
        return render(request,'buyer/add_bank_details.html')
    def post(self,request):
        return render(request,'buyer/add_bank_details.html')
class Add_upi(View):
    def get(self,request):
        return render(request,'buyer/add_upi.html')
    def post(self,request):
        return render(request,'buyer/add_upi.html')

class My_payments(View):
    def get(self,request):
        return render(request,'buyer/my_payments.html')
    def post(self,request):
        return render(request,'buyer/my_payments.html')