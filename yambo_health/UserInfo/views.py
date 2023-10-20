from rest_framework import generics
from .models import Patient,BloodPressure,Weight,BloodGlucose
from .serializers import UserSerializer,BloodPressureSerializer,WeightSerializer,BloodGlucoseSerializer



class UserList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = UserSerializer

class BpCreate(generics.CreateAPIView):
    queryset = BloodPressure.objects.all()
    serializer_class = BloodPressureSerializer

class BpList(generics.ListAPIView):
    queryset = BloodPressure.objects.all()
    serializer_class = BloodPressureSerializer


class BpDetail(generics.ListAPIView):
    serializer_class = BloodPressureSerializer

    def get_queryset(self):
        custom_field_value = self.kwargs['userId']  # Use the custom field value from the URL
        user_id = self.request.query_params.get('userId')
        queryset = BloodPressure.objects.filter(userId=custom_field_value)

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset

class WeightCreate(generics.CreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

class WeightList(generics.ListAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


class WeightDetail(generics.ListAPIView):
    serializer_class = WeightSerializer

    def get_queryset(self):
        custom_field_value = self.kwargs['userId']  # Use the custom field value from the URL
        user_id = self.request.query_params.get('userId')
        queryset = Weight.objects.filter(userId=custom_field_value)

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset


class BloodGlucoseDetail(generics.ListAPIView):
    serializer_class = BloodGlucoseSerializer

    def get_queryset(self):
        custom_field_value = self.kwargs['userId']  # Use the custom field value from the URL
        user_id = self.request.query_params.get('userId')
        queryset = BloodGlucose.objects.filter(userId=custom_field_value)

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset


class BloodGlucoseCreate(generics.CreateAPIView):
    queryset = BloodGlucose.objects.all()
    serializer_class = BloodPressureSerializer


class BloodGlucoseList(generics.ListAPIView):
    queryset = BloodGlucose.objects.all()
    serializer_class = BloodPressureSerializer

class BloodGlucoseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodGlucose.objects.all()
    serializer_class = BloodGlucoseSerializer