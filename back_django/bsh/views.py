from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bsh.models import Bsh
from bsh.serializers import BshSerializer

#################################################################
# Decorator based vs class based
#################################################################

# @api_view(['GET', 'POST'])
# def bsh_list(request, format=None):
#     if request.method == 'GET':
#         bsh = Bsh.objects.all()
#         serializer = BshSerializer(bsh, many=True)
#         return Response(serializer.data)

    
#     elif request.method == 'POST':
#         serializer = BshSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,
#                             status=status.HTTP_201_CREATED)
    

class BshList(generics.ListCreateAPIView):
    queryset = Bsh.objects.all()
    serializer_class = BshSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def bsh_detail(request, pk, format=None):
#     try:
#         bsh = Bsh.objects.get(pk=pk)
#     except Bsh.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

    
#     if request.method == 'GET':
#         serializer = BshSerializer(bsh)
#         return Response(serializer.data)

    
#     elif request.method == 'PUT':
#         serializer = BshSerializer(bsh, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, 
#                         status=status.HTTP_400_BAD_REQUEST)


#     elif request.method == 'DELETE':
#         bsh.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class BshDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bsh.objects.all()
    serializer_class = BshSerializer