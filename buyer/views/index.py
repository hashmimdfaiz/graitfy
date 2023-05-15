from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
class Homepage(View):
    def get(self,request):
        return render(request,'buyer/homepage.html')
    def post(self,request):
        return render(request,'buyer/homepage.html')