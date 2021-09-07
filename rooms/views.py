from math import ceil
from django.views.generic import ListView
from . import models


#reference-> ccbv.co.uk 
class HomeView(ListView):
    
    
    """ HomeView Definition """
    
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"