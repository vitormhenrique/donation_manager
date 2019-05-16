from django.urls import path

from donation_manager.transport_order.views import (
    transport_order_list_view,
    items_without_destination_view,
)

app_name = "transport_order"
urlpatterns = [
    path("", view=transport_order_list_view, name="transport_order_list"),
    path("/assign_destination", view=items_without_destination_view, name="items_without_destination"),
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
