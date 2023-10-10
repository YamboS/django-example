from django.contrib import admin
from .models import BloodPressure,User,Weight
# Register your models here.
admin.site.register(BloodPressure)
admin.site.register(User)
admin.site.register(Weight)