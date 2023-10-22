from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
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


class BpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weight.objects.all()
    serializer_class = BloodPressureSerializer

class WeightCreate(generics.CreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

class WeightList(generics.ListAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


class WeightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)

            # Retrieve the updated data
            updated_data = Weight.objects.all()

            # Serialize the updated data
            serialized_data = WeightSerializer(updated_data, many=True).data

            return Response({'data': serialized_data}, status=status.HTTP_200_OK)
        except Weight.DoesNotExist:
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BloodGlucoseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weight.objects.all()
    serializer_class = BloodGlucoseSerializer

class BloodGlucoseCreate(generics.CreateAPIView):
    queryset = BloodGlucose.objects.all()
    serializer_class = BloodPressureSerializer


class BloodGlucoseList(generics.ListAPIView):
    queryset = BloodGlucose.objects.all()
    serializer_class = BloodPressureSerializer

class BloodGlucoseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BloodGlucose.objects.all()
    serializer_class = BloodGlucoseSerializer