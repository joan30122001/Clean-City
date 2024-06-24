from django.contrib import admin
from .models import EmergencyCollection, Payment, Profile, CompanyProfile, IllegalDeposit, Payment



admin.site.register(Profile)
admin.site.register(CompanyProfile)
admin.site.register(EmergencyCollection)
admin.site.register(IllegalDeposit)
admin.site.register(Payment)