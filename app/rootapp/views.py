from django.db.models import Q
from django.db.models.query import QuerySet
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from collections import namedtuple
from rootapp.models import Country,Region,City
from rootapp import serializers
from rootapp.utils.DistanceCalculator import DistanceCalculator


class MyFilterView():
    """
    My filter that can be used in all  ListCreateAPIView classes
    Filters the models by name, and it can sort them by a given model distance
    """
    @staticmethod
    def genericFilterByNameAndDistance( model, queryset_list, request):
            queryset_list = queryset_list
            # We take the request parameters if exists
            query_name = request.GET.get('name')
            query_model_id = request.GET.get('id')

            # if the request parameter exists and its length is more than 2 letters
            # filters the queryset_list
            if query_name and len(query_name)>=3:
                queryset_list = queryset_list.filter(
                    Q(name__icontains=query_name)
                )
            
            # if the request parameter 'id' exists sorts the queryset_list
            if query_model_id:
                # Get the model with the given id from the database
                selectedModel = model.objects.get(pk=query_model_id)
                models = model.objects.exclude(id= query_model_id)
                distances_list =[]

                # Fill the distances_list list with tuples (the model, and its distance from the selected model)
                for model in models:
                    distance= DistanceCalculator.calculate(selectedModel, model)
                    distances_list.append( (model, distance) )

                # Sort distances_list by distance from the selected model
                distances_list= sorted(distances_list, key=lambda model: model[1])
                result =[]

                #fill the result list with the sorted models
                for model in distances_list:
                    result.append(model[0])
                return result
            
            return queryset_list


class CountryModelViewSet(ModelViewSet):
    """
    Manage List and Create for countries
    - To get all countries send GET request to http://127.0.0.1:8000/api/countries/
    - To get a country with a specific id, send GET request to http://127.0.0.1:8000/api/countries/ID
    - To get all countries based on a string query of more than 3 characters send GET request,
      with "name" as query parameter to http://127.0.0.1:8000/api/countries?name=STRING
    - To get the nearest countries in relation to a given country send GET request, with "countryId"
      as query parameter to http://127.0.0.1:8000/api/countries?countryId=ID
    - You can combine the query parameters to filter your search http://127.0.0.1:8000/api/countries?name=STRING&countryId=ID
    - To create a new country, send POST request to http://127.0.0.1:8000/api/countries/ , with your JASON data in the request body
    """
    queryset_list = Country.objects.all()
    serializer_class = serializers.CountrySerializer

    def get_queryset(self, *args, **kwargs):
        return MyFilterView.genericFilterByNameAndDistance(Country, self.queryset_list, self.request)


class RegionModelViewSet(ModelViewSet):
    """
    Manage List and Create for regions
    - To get all regions send GET request to http://127.0.0.1:8000/api/regions/
    - To get a region with a specific id, send GET request to http://127.0.0.1:8000/api/regions/ID
    - To get all regions based on a string query of more than 3 characters send GET request,
      with "name" as query parameter to http://127.0.0.1:8000/api/regions?name=STRING
    - To get the nearest regions in relation to a given region send GET request, with "regionId"
      as query parameter to http://127.0.0.1:8000/api/regions?regionId=ID
    - You can combine the query parameters to filter your search http://127.0.0.1:8000/api/regions?name=STRING&regionId=ID
    - To create a new region, send POST request to http://127.0.0.1:8000/api/regions/ , with your JASON data in the request body
    """
    queryset_list = Region.objects.all()
    serializer_class = serializers.RegionSerializer

    def get_queryset(self, *args, **kwargs):
        return MyFilterView.genericFilterByNameAndDistance(Region, self.queryset_list, self.request)


class CityModelViewSet(ModelViewSet):
    """
    Manage List and Create for cities
    - To get all cities send GET request to http://127.0.0.1:8000/api/cities/
    - To get a city with a specific id, send GET request to http://127.0.0.1:8000/api/cities/ID
    - To get all cities based on a string query of more than 3 characters send GET request,
      with "name" as query parameter to http://127.0.0.1:8000/api/cities?name=STRING
    - To get the nearest cities in relation to a given city send GET request, with "cityId"
      as query parameter to http://127.0.0.1:8000/api/cities?cityId=ID
    - You can combine the query parameters to filter your search http://127.0.0.1:8000/api/cities?name=STRING&cityId=ID
    - To create a new city, send POST request to http://127.0.0.1:8000/api/cities/ , with your JASON data in the request body
    """
    queryset_list = City.objects.all()
    serializer_class = serializers.CitySerializer

    def get_queryset(self, *args, **kwargs):
        return MyFilterView.genericFilterByNameAndDistance(City, self.queryset_list, self.request)


class FilterNameViewSet(ViewSet):
    """
    A simple ViewSet for listing the Tweets and Articles in your Timeline.
    """
    # queryset = Snippet.objects.all()
    nameFilter = namedtuple('name_filter', ('countries', 'regions','cities'))
    def list(self, request):
        query_name = request.GET.get('name')
        name_filter_result = ' '
        if query_name and len(query_name)>=3:
            name_filter_result = self.nameFilter(
                countries=Country.objects.filter( Q(name__icontains=query_name)),
                regions=Region.objects.filter( Q(name__icontains=query_name)),
                cities=City.objects.filter( Q(name__icontains=query_name)),
            )
        else: 
            name_filter_result = self.nameFilter(
                    countries=Country.objects.all(),
                    regions=Region.objects.all(),
                    cities=City.objects.all(),
                )

        serializer = serializers.NameFilterSerializer(name_filter_result)
        return Response(serializer.data)