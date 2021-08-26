from django.core.management.base import BaseCommand
from rootapp.models import Country, Region, City


class Command(BaseCommand):
    """Command to delete the dummy data from the database"""

    def handle(self, *args, **kwargs):
        #Creating countries
        Country.objects.all().delete()
        Region.objects.all().delete()
        City.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('The dummy data were deleted!'))