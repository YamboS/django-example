from django.contrib import admin
from .models import BloodPressure,Patient,Weight
# Register your models here.
admin.site.register(BloodPressure)
admin.site.register(Patient)
admin.site.register(Weight)