from django.contrib import admin

from apps.doctors.models import MedicalSpeciality, MedicalProfessional


class MedicalSpecialityAdmin(admin.ModelAdmin):
    pass


class MedicalProfessionalAdmin(admin.ModelAdmin):
    pass


admin.site.register(MedicalSpeciality, MedicalSpecialityAdmin)
admin.site.register(MedicalProfessional, MedicalProfessionalAdmin)
