from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Min
from django.db.models import Max
from transport.models import Transport
from transport.api.serializers import TransportSerializer

#API VIEW das viagens
@api_view(['GET'])
def transport_detail_api_view(request, city):
    #lança exceção se não achar a cidade requerida
    try:
        transport = Transport.objects.filter(city=city)
    except Transport.DoesNotExist:
        return Response({"Error":{
            "code":404,
            "message":"City not found"
        }},status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        #pega a query ordena por a maior duracao e seleciona o primeiro
        econ = transport.order_by('-price_econ').first()
        #pega a query ordena por maior preco conforto e orderna pelo menor duracao
        conf = transport.order_by('-duration').first()
        #serializa as querys
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
        #O SQLITE nao tem suporte para a função distinct do django então
        #Criei um set de cidades e a lista de transport
        #para cada transporte em transportes, se o destino da viagem nao estiver
        #no conjunto de cidades adiciona a lista de transportes e adicione ao
        #ao conjunto a cidade do transporte
        transport_unique = []
        cities_set = set()
        for transport in transports:
            if transport.city not in cities_set:
                transport_unique.append(transport) 
                cities_set.add(transport.city)

        serializer = TransportSerializer(transport_unique, many=True)
        return Response(serializer.data)
