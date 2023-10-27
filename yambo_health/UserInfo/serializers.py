from rest_framework import serializers
from .models import Patient,BloodPressure,Weight,BloodGlucose

class BloodPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPressure
        fields = ["userId","recordIdBp","systolicPress","diastolicPress","bpm","datetime"]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["recordIdBp","patientId","datetime","user","password","recordIdBp","recordIdW","recordIdBg"]

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ["recordIdW","userId","weightLb","bmi","datetime"]

class BloodGlucoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodGlucose
        fields = ["userId","recordIdBg","blood_sugar_level","datetime"]