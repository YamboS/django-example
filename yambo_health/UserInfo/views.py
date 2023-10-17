from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Patient,BloodPressure,Weight
from .serializers import UserSerializer,BloodPressureSerializer,WeightSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def user_details(request, pk):
#     """
#     Retrieve, update or delete a user.
#     """
#     try:
#         user = Patient.objects.get(pk=pk)
#
#     except Patient.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET','POST'])
# def all_user_details(request):
#         """
#         Retrieve, update or delete a user.
#         """
#         user = Patient.objects.all()
#         serializer = UserSerializer(user,many=True)
#         return Response(serializer.data)


# @api_view(['POST'])
# def create_user(request):
#         """
#         CREATE a user.
#         """
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#


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