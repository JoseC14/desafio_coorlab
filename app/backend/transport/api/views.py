from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Min
from django.db.models import Max
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
        econ = transport.annotate(Min('price_econ'),Max('duration')).order_by('-price_econ').first()
        print(f"ECONOMICA {econ}")
        conf = transport.annotate(Max('price_confort'),Min('duration')).order_by('price_confort').first()
        serializer_econ = TransportSerializer(econ)
        serializer_conf = TransportSerializer(conf)
        return Response({'transports':[            
                         serializer_conf.data,
                         serializer_econ.data
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
