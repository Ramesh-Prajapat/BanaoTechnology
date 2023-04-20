from django.contrib import admin
from .models import Doctor, Patient

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'profile_picture', 'username', 'email','address', 'password', 'confirm_password')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'profile_picture', 'username', 'email','address', 'password', 'confirm_password')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)