from django.shortcuts import render, redirect
from donation_manager.donation.models import Donation
from donation_manager.transport_order.models import Transport_Order, AvailableTime
from django.http import JsonResponse


def create_donation(request):

    if request.method == "POST":

        donated_item_name = request.POST.get("donated_item_name")
        donated_item_description = request.POST.get("donated_item_description")
        donated_item_weight = request.POST.get("donated_item_weight")
        donated_item_dimension = request.POST.get("donated_item_dimension")
        donated_item_address = request.POST.get("donated_item_address")

        transport_order_day = request.POST.getlist("transport_order_day[]")
        transport_order_start_time = request.POST.getlist("transport_order_start_time[]")
        transport_order_end_time = request.POST.getlist("transport_order_end_time[]")

        donation = Donation()
        donation.name = donated_item_name
        donation.description = donated_item_description
        donation.weight = donated_item_weight
        donation.dimension = donated_item_dimension
        donation.status = Donation.WAITING_CLAIM
        donation.save()

        transport_order = Transport_Order()
        transport_order.origin = donated_item_address
        transport_order.donated_item = donation
        transport_order.transit_status = Transport_Order.WAITING_DESTINATION_DEFINITION
        transport_order.save()

        for counter, value in enumerate(transport_order_day):
            
            day_code = AvailableTime.get_day_code(value)

            available_time = AvailableTime()
            available_time.day_of_week = day_code
            available_time.start_time = transport_order_start_time[counter]
            available_time.end_time = transport_order_end_time[counter]
            available_time.transport_order = transport_order
            available_time.save()


        return JsonResponse({'message': 'success'})
 
    return render(request, 'donation/index.html')
