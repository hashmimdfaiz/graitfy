from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from buyer.models.registrations import User, OTP
import random

# Create your views here.
class Login(View):
    def get(self,request):
        return render(request,'buyer/login.html')
    def post(self,request):
        phone_number = request.POST.get('phone_num')
        get_otp = OTP.get_otp_phone(phone_number)
        if get_otp:
            if User.get_user_phone(phone_number):
                request.session['buyer_phone_num'] = phone_number
                redirect('buyer_otp',user_type = 'login')
            else:
                redirect('buyer_otp',user_type = 'Register')
        else:
            if User.get_user_phone(phone_number):
                otp = random.randint(10000, 99999)
                OTP(
                    phone_number=phone_number,
                    otp=otp
                ).save()
                request.session['buyer_phone_num'] = phone_number
                redirect('buyer_otp',user_type = 'login')
            else:
                otp = random.randint(10000, 99999)
                OTP(
                    phone_number=phone_number,
                    otp=otp
                ).save()
                request.session['buyer_phone_num'] = phone_number
                redirect('buyer_otp',user_type = 'Register')
        return render(request,'buyer/login.html')
class Otp(View):
    def get(self,request,user_type):
        # if 'gis' in user_type or 'in' in user_type:

        return render(request,'buyer/otp.html')
    def post(self,request,user_type):
        return render(request,'buyer/otp.html')

class Logout(View):
    def get(self,request):
        return redirect('buyer_homepage')
    # def post(self,request):
    #     return render(request,'buyer/otp.html')