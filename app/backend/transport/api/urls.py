from django.urls import path
from transport.api.views import transport_detail_api_view
from transport.api.views import transport_list_api_view

urlpatterns =[
    #URL para listar transportes
     path("transports/", transport_list_api_view, name='transport_list'),
     
    #URL para retornar a viagem mais economica e a mais confortavel
    path("transports/<str:city>/",transport_detail_api_view,
         name='transport_detail') 
]