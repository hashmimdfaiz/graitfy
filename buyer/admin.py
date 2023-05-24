from django.contrib import admin
from buyer.models.registrations import User, OTP

# Register your models here.

class For_users(admin.ModelAdmin):
    list_display = ['name','phone_number']
class For_users_otp(admin.ModelAdmin):
    list_display = ['phone_number','otp']

admin.site.register(User,For_users)
admin.site.register(OTP,For_users_otp)