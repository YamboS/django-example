from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient,BloodPressure,Weight
from .serializers import UserSerializer,BloodPressureSerializer,WeightSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        user = Patient.objects.get(pk=pk)

    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def all_user_details(request):
        """
        Retrieve, update or delete a user.
        """
        user = Patient.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)