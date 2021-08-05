from rest_framework.decorators import api_view
from rest_framework.response import Response

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
            'Endpoint': '/rooms/update/{id}',
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