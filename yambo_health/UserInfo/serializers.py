from rest_framework import serializers
from .models import Patient,BloodPressure,Weight

class BloodPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPressure
        fields = ["patientId","systolicPress","diastolicPress","bpm","datetime"]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["patientId","datetime","user","password","bpId","weightId"]

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ["userId","weightLb","bmi","datetime"]