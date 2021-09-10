from math import ceil
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


#reference-> ccbv.co.uk 
class HomeView(ListView):
    
    
    """ HomeView Definition """
    
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"
    

class RoomDetail(DetailView):
    
    """ RoomDetail Definition """
    
    template_name = "rooms/room_detail.html"
    model = models.Room
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         # return redirect(reverse("core:home"))
#         raise Http404()
        
def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})