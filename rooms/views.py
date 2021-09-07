from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

def all_rooms(request):
    
    page = request.GET.get("page")
#    query set is lazy. just make queryset and it will be called later. so here, it's fine to do this 
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", {"rooms":rooms})
    
    # page = request.GET.get("page")
    # page = int(page or 1)

    # page_size = 10
    # limit = page_size*page
    # offset = limit - page_size
    # all_rooms = models.Room.objects.all()[offset:limit]
    
    # page_count = ceil(models.Room.objects.count()/page_size)
                      
    # return render (
    #     request,
    #     "rooms/home.html",
    #     {
    #         "potato": all_rooms,
    #         "page":page,
    #         "page_count": page_count,
    #         "page_range": range(1, page_count),
    #     },
    # )