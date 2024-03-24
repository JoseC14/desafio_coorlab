# Resultado - Desáfio CoorLab

## Estrutura das pastas

Primeiro comecei estruturando as pastas, separando o backend do frontend preferi
chamar o nome das pastas de backend para a construção da API e comunicação com o
banco de dados e frontend para aplicação vue

# Back-End com Django Rest Framework

## Construção da Api e banco de dados

Comecei fazendo a model do banco de dados com base no json que foi fornecido, e fiz as migrações pra o banco de dados. então usei o django rest framework para construção da api, criei um pasta chamada api(app/backend/transports/api) para fazer a mesma, depois, fiz o serializers com os campos necessários e aí fui fazer as views, que estruturei da seguinte forma: view para listar os destinos; view para mostrar as viagens quando o usuário selecionasse a data e a cidade retornasse as melhores viagens 

# Front-end com Vue

 Iniciei fazendo a sidebar como mostrado no protótipo, depois fui fazer o FormTravel que iria ter o formulario para o usuario interagir com os campos, então fiz o PassTravel onde mostra o card das melhores viagens.
 Depois de ter feito isso, comecei fazendo a comunicacao com a api, onde deu tudo certo, agora só faltava validar os campos, criei uma ModalError informando ao usuário que ele deveria preencher os campos

