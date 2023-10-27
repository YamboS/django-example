from django.db import models

class Patient(models.Model):
    patientId = models.AutoField(primary_key=True,)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    recordIdBp = models.ForeignKey("BloodPressure", on_delete=models.PROTECT, null=True, to_field='recordIdBp')
    recordIdW = models.ForeignKey("Weight", on_delete=models.PROTECT, null=True, to_field='recordIdW')
    recordIdBg = models.ForeignKey("BloodGlucose", on_delete=models.PROTECT, null=True, to_field='recordIdBg')

    def __str__(self):
        return self.user

class BloodPressure(models.Model):
    userId = models.ForeignKey("Patient",on_delete=models.CASCADE,null=True,to_field='patientId')
    recordIdBp = models.AutoField(primary_key=True, )
    systolicPress = models.IntegerField(null=True)
    diastolicPress = models.IntegerField(null=True)
    bpm = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True,)


class Weight(models.Model):
    userId = models.ForeignKey("Patient",on_delete=models.CASCADE,null=True)
    recordIdW = models.AutoField(primary_key=True,)
    weightLb = models.DecimalField(max_digits=4,decimal_places=1)
    bmi = models.DecimalField(null=True, blank=True,max_digits=4,decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)

class BloodGlucose(models.Model):
    userId = models.ForeignKey("Patient",on_delete=models.CASCADE,null=True,to_field='patientId')
    recordIdBg = models.AutoField(primary_key=True,)
    blood_sugar_level = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True,)






