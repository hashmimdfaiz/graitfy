from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib import messages
from buyer.models.registrations import User

# Create your views here.
class Profile(View):
    def get(self,request):
        return render(request,'buyer/profile_update.html')
    def post(self,request):
        first_name = request.POST.get('first_name').capitalize()
        last_name = request.POST.get('last_name').capitalize()
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(first_name + ' ' + last_name + ' ' + email)
       
        if password1 != password2:
            print("Not Match")
            messages.error(request, "Password does not match")
            return render('buyer_profile')
        else:
            customer = request.session.get('customer')
            try:
                user = User.objects.get(id=customer)
            except User.DoesNotExist:
                messages.error("User not found")
                return redirect('login')
            
        
        

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