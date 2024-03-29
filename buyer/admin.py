from django.contrib import admin
from buyer.models.registrations import User, OTP
from buyer.models.help import Help

# Register your models here.

class For_users(admin.ModelAdmin):
    list_display = ['name','phone_number']
class For_users_otp(admin.ModelAdmin):
    list_display = ['phone_number','otp']

class For_users_help(admin.ModelAdmin):
    list_display = ['phone_number','related_issue']

admin.site.register(User,For_users)
admin.site.register(OTP,For_users_otp)
admin.site.register(Help,For_users_help)