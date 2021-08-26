from django.test import TestCase
from django.urls import reverse
from django.db.models import Q
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status
from rootapp.models import Country
from rootapp.serializers import CountrySerializer

CREATE_COUNTRY_URL = reverse('rootapp:countries-list')

payload_Greece = {
            "name":"Greece",
            "latitude":"38.2749497",
            "longitude": "23.8102717"
        }
payload_France = {
            "name":"France",
            "latitude":"46.71109",
            "longitude":"20.546151"
        }

def create_Greece():
    return Country.objects.create(
            name="Greece",
            latitude=38.2749497,
            longitude= 23.8102717
        )

def create_France():
    return Country.objects.create(
            name="France",
            latitude=46.71109,
            longitude=1.7191036
        )

def create_HongKong():
    return Country.objects.create(
            name="Hong Kong",
            latitude=22.3700556,
            longitude= 114.1535941
        )

def create_Ukraine():
    return Country.objects.create(
            name="Ukraine",
            latitude=48.383022,
            longitude= 31.1828699
        )

def detail_url(country_id):
    """Return recipe detail URL"""
    return reverse('rootapp:countries-detail', args=[country_id])

def filter_by_distance_url(country_id):
    """Return recipe detail URL"""
    return reverse('rootapp:places-detail', args=[country_id])


class CountryApiTests(TestCase):
    """Test the countries api"""

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def test_create_valid_country_success(self):
        """Test creating country with valid payload is successful"""

        result = self.client.post(CREATE_COUNTRY_URL, payload_Greece)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        
    def test_country_exists(self):
        """Test creating a country that already exists fails"""
        
        self.client.post(CREATE_COUNTRY_URL,payload_Greece)
        result = self.client.post(CREATE_COUNTRY_URL,payload_Greece)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_countries(self):
        """Test retrieving a list of countries"""
        create_France()
        create_Greece()
        result = self.client.get(CREATE_COUNTRY_URL)
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data, serializer.data)

    def test_partial_update_country(self):
        """Test updating a field in country"""
        france = create_France()
        url = detail_url(france.id)
        result = self.client.patch(url,payload_France)
        france.refresh_from_db()
        serializer = CountrySerializer(france)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertAlmostEqual(float(serializer['longitude'].value),  float(payload_France['longitude']), 6)

    def test_full_update_country(self):
        """Test updating full country"""
        france = Country.objects.create(
                        name="FALSE_France",
                        latitude=58.71109,
                        longitude=15.7191036
                    )
        url = detail_url(france.id)
        result = self.client.put(url,payload_France)
        france.refresh_from_db()
        serializer = CountrySerializer(france)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer['name'].value,  payload_France['name'])
        self.assertAlmostEqual(float(serializer['latitude'].value),  float(payload_France['latitude']), 6)
        self.assertAlmostEqual(float(serializer['longitude'].value),  float(payload_France['longitude']), 6)

    def test_get_all_countries_by_str_query(self):
        """Test getting countries by query string that has more than 2 letters"""
        create_France()
        create_Greece()
        query_str = "ree"
        queryset_list = Country.objects.filter(Q(name__icontains=query_str))
        result = self.client.get(  CREATE_COUNTRY_URL, {'name': query_str})
        serializer = CountrySerializer(queryset_list, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data, serializer.data)
        
    def test_get_countries_by_distance(self):
        """Test getting a list with countries sorted by distance from France"""
        create_Ukraine()
        france = create_France()
        create_Greece()
        create_HongKong()
        queryset_list = Country.objects.all()
        result = self.client.get(  CREATE_COUNTRY_URL, {'id': france.id})
        serializer = CountrySerializer(queryset_list, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertNotEqual(result.data, serializer.data)