from django.shortcuts import render
from .models import Transport_Order

# Create your views here.


def transport_order_list_view(request):
    queryset = Transport_Order.objects.all() # list of objects

    print(queryset)
    
    context = {
        "object_list": queryset
    }
    return render(request, "transport_order/transport_order_list.html", context)