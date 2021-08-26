from django.core.management.base import BaseCommand
from rootapp.models import Country, Region, City


class Command(BaseCommand):
    """Command to create dummy data to the database"""

    def handle(self, *args, **kwargs):
        #Creating countries
        greece = Country.objects.create(
                        name="Greece",
                        latitude=38.2749497,
                        longitude= 23.8102717
                    )
        france = Country.objects.create(
                    name="France",
                    latitude=46.71109,
                    longitude=1.7191036
                )
        iceland = Country.objects.create(
                    name="Iceland",
                    latitude=64.98418,
                    longitude= -18.10590
                )
        germany = Country.objects.create(
                    name="Germany",
                    latitude = 51.08342,
                    longitude = 10.42345
                )
        # Create Regions
        attica = Region.objects.create(
            country = greece,
            name = "Attica",
            latitude = 37.99465,
            longitude = 23.79940
        )
        island_of_France = Region.objects.create(
            country = iceland,
            name = "Island of France",
            latitude = 48.64431,
            longitude = 2.75379
        )
        western_region = Region.objects.create(
            country = france,
            name = "Western Region",
            latitude = 64.89595,
            longitude = -22.15484
        )
        lower_saxony = Region.objects.create(
            country = germany,
            name = "Lower Saxony",
            latitude = 64.89595,
            longitude = -22.15484
        )
        # Create Cities 
        athens = City.objects.create(
            region = attica,
            name = "Athens",
            latitude = 37.98394,
            longitude = 23.72831
        )
        paris = City.objects.create(
            region = island_of_France,
            name = "Paris",
            latitude = 37.98394,
            longitude = 23.72831
        )
        akranes = City.objects.create(
            region = western_region,
            name = "Akranes",
            latitude = 64.31708,
            longitude = -22.08335
        )
        hanover = City.objects.create(
            region = lower_saxony,
            name = "Hanover",
            latitude = 48.85670,
            longitude = 2.35146
        )
        self.stdout.write(self.style.SUCCESS('The dummy data were created!'))