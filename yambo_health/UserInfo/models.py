from django.db import models

class User(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    username = models.CharField()
    password = models.CharField()
    userId = models.IntegerField(primary_key=True)
    bpId = models.ForeignKey("BloodPressure",on_delete=models.CASCADE,)
    weightId = models.ForeignKey("Weight",on_delete=models.CASCADE,)


    def __str__(self):
        return self.name

class BloodPressure(models.Model):
    bpId = models.IntegerField(primary_key=True)
    systolicPress = models.IntegerField()
    diastolicPress = models.IntegerField()
    bpm = models.IntegerField()
    userId = models.ForeignKey("User",on_delete=models.DO_NOTHING,)
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Weight(models.Model):
    weightLb = models.DecimalField()
    bmi = models.DecimalField(null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    weightId = models.IntegerField(primary_key=True)
    userId = models.ForeignKey("User",on_delete=models.DO_NOTHING,)


    def __str__(self):
        return self.name


