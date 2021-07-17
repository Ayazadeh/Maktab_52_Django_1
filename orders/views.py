from django.views.generic import ListView

from orders.models import Orders


class Order(ListView):
    model = Orders
    template_name = "orders.html"
