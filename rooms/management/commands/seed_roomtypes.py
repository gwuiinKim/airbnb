from django.core.management.base import BaseCommand
from rooms.models import RoomType

class Command(BaseCommand):

    help = "This command creates room types"


    def handle(self, *args, **options):
        room_types = [
           "Hotel room",
           "Private room",
           "Share room",
           "Entire place",
        ]
        for room_type in room_types:
            RoomType.objects.create(name=room_type)
            
        self.stdout.write(self.style.SUCCESS("RoomType created!"))
            