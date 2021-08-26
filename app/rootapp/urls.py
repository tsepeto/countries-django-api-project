from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rootapp import views

router = DefaultRouter()
router.register('places', views.FilterNameViewSet,basename='places')
router.register('countries', views.CountryModelViewSet, basename ='countries')
router.register('regions', views.RegionModelViewSet, basename ='regions')
router.register('cities', views.CityModelViewSet, basename ='cities')

app_name = 'rootapp'

urlpatterns = [
    path('', include(router.urls)),
]
