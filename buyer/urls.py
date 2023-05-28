"""
URL configuration for grabitfy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from buyer.views.index import Homepage, Spin_reward
from buyer.views.profile import Profile, Help, Add_bank_details, Add_upi, My_payments
from buyer.views.login import Login, Otp, Logout
from buyer.views.cart import Cart, Place_order, Payment_order_place
# from seller.urls import

urlpatterns = [
    path('',Homepage.as_view(),name = 'buyer_homepage'),
    path('profile/',Profile.as_view(),name = 'buyer_profile'),
    path('signup/',Homepage.as_view(),name = 'buyer_signup'),
    path('login/',Login.as_view(),name = 'buyer_login'),
    path('otp/',Otp.as_view(),name = 'buyer_otp'),
    path('help/',Help.as_view(),name = 'buyer_help'),
    path('addbankdetails/',Add_bank_details.as_view(),name = 'buyer_add_bank_details'),
    path('addupi/',Add_upi.as_view(),name = 'buyer_add_upi'),
    path('my_payments/',My_payments.as_view(),name = 'buyer_my_payments'),
    path('spin_reward/',Spin_reward.as_view(),name = 'buyer_spin_reward'),
    path('cart/',Cart.as_view(),name = 'buyer_cart'),
    path('place_order/',Place_order.as_view(),name = 'buyer_place_order'),
    path('order_payment_details/',Payment_order_place.as_view(),name = 'buyer_payment_place_order'),
    path('logout/',Logout.as_view(),name = 'buyer_logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)