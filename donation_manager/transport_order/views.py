from django.shortcuts import render
from .models import Transport_Order
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from donation_manager.users.models import User
from donation_manager.donation.models import Institution

# Create your views here.



def transport_order_list_view(request):
    transport_order_queryset = Transport_Order.objects.all() # list of objects
    # queryset = Transport_Order.get_all_waiting_destination()    
    # queryset = Transport_Order.get_all_waiting_driver_assignment()    
    context = {
        "transport_order_list": transport_order_queryset
    }
    return render(request, "transport_order/transport_order_list.html", context)

@login_required
def items_without_destination_view(request):    

    user = request.user

    institution_list = user.institution_set.all()
    print(institution_list)

    if request.method == "POST":
        institution_id = request.POST.getlist("selected_institution")
        institution = get_object_or_404(Institution, institution_id)

        selected_transport_orders_ids = request.POST.getlist("selected_transport_orders")

        # print(selected_transport_orders_ids)
        
        for transport_order_id in selected_transport_orders_ids:
            transport_order = get_object_or_404(Transport_Order, transport_order_id)
            transport_order.destination = institution.address
            transport_order.transit_status = Transport_Order.WAITING_DRIVER_ASSIGNMENT
    
    transport_order_queryset = Transport_Order.get_all_waiting_destination()    
    
    context = {
        "transport_order_list": transport_order_queryset,
        "institution_list": institution_list,
    }
    return render(request, "transport_order/assign_destination.html", context)