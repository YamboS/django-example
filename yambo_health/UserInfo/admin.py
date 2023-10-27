from django.contrib import admin
from .models import BloodPressure,Patient,Weight,BloodGlucose
# Register your models here.
admin.site.register(BloodPressure)
admin.site.register(Patient)
admin.site.register(Weight)
admin.site.register(BloodGlucose)