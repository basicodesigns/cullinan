from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import serializer_helpers
from .serializers import CottageSerializer, RoomSerializer
from .models import Cottage, Room




@api_view(['GET'])
def getRoutes(response):
    routes = [
        {
            'Endpoint': '/rooms/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a array of rooms cottages'
        },
        {
            'Endpoint': '/rooms/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single of room cottage'
        },
        {
            'Endpoint': '/rooms/add',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Adds a room'
        },
        {
            'Endpoint': '/rooms/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates a rooms cottages'
        },
        {
            'Endpoint': '/rooms/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing rooms'
        }
    ]
    return Response(routes)


# Start of Cottages CRUD
@api_view(['POST'])
def addCottage(request):
    serializer = CottageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAllCottages(request):
    cottages = Cottage.objects.all()
    serializer = CottageSerializer(cottages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCottageById(request, pk):
    try:
        cottage = Cottage.objects.get(id=pk)
    except Cottage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CottageSerializer(cottage, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateCottageById(request, pk):
    try:
        cottage = Cottage.objects.get(id=pk)
    except Cottage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CottageSerializer(cottage, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteCottageById(request, pk):
    try:
        cottage = Cottage.objects.get(id=pk)
    except Cottage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    cottage.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# End of Cottages


# Start of Rooms CRUD
@api_view(['POST'])
def addRoom(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAllRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoomById(request, pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateRoomById(request, pk):
    try:
        cottage = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = RoomSerializer(cottage, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteRoomById(request, pk):
    try:
        cottage = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    cottage.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# End of Rooms