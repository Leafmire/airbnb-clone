from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This commnad creates amenities"

    """    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        ) """

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Wifi",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop friendly workspace",
            "TV",
            "Private bathroom",
            "Washer",
            "Dryer",
            "Breakfast",
            "Indoor fireplace",
            "Crib",
            "High chair",
            "Self check-in",
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
            "Beachfront",
            "Waterfront",
            "Ski-in/ski-out",
            "Smoke detector",
            "Carbon monoxide detector",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
