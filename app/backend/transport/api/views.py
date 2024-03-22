from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Min
from transport.models import Transport
from transport.api.serializers import TransportSerializer


@api_view(['GET'])
def transport_detail_api_view(request, city):
    try:
        transport = Transport.objects.filter(city=city)
    except Transport.DoesNotExist:
        return Response({"Error":{
            "code":404,
            "message":"City not found"
        }},status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        econ = transport.annotate(econ=Min('price_econ')).first()
        conf = transport.annotate(econ=Min('price_confort')).first()
        serializer_econ = TransportSerializer(econ)
        serializer_conf = TransportSerializer(conf)
        return Response({'transports':[
                         serializer_econ.data,
                         serializer_conf.data
                        ]
                         })


@api_view(['GET'])
def transport_list_api_view(request):

    try:
        transports = list(set(Transport.objects.all()))
    except Transport.DoesNotExist:
        return Response({"Error":{
            "code":404,
            "message":"City not found"
        }},status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        transport_unique = []
        cities_set = set()
        for transport in transports:
            if transport.city not in cities_set:
                transport_unique.append(transport) 
                cities_set.add(transport.city)
     
        serializer = TransportSerializer(transport_unique, many=True)
        return Response(serializer.data)
