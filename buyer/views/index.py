from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
class Homepage(View):
    def get(self,request):
        return render(request,'buyer/home.html')
    def post(self,request):
        return render(request,'buyer/home.html')
class Spin_reward(View):
    def get(self,request):
        return render(request,'buyer/spin_reward.html')
    def post(self,request):
        return render(request,'buyer/spin_reward.html')
class Categories(View):
    def get(self,request):
        return render(request,'buyer/categories.html')
    def post(self,request):
        return render(request,'buyer/categories.html')