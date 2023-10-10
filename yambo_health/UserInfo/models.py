from django.db import models

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    bpId = models.IntegerField(null=True)
    weightId = models.IntegerField(null=True)

    def __str__(self):
        return self.user

class BloodPressure(models.Model):
    userId = models.ForeignKey("User",on_delete=models.CASCADE,null=True)

    systolicPress = models.IntegerField(null=True)
    diastolicPress = models.IntegerField(null=True)
    bpm = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True,)


class Weight(models.Model):
    userId = models.ForeignKey("User",on_delete=models.CASCADE,null=True)

    weightLb = models.DecimalField(max_digits=4,decimal_places=1)
    bmi = models.DecimalField(null=True, blank=True,max_digits=4,decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)





