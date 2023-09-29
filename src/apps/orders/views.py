import json

from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from src.apps.customers.models import Customer
from src.apps.orders.models import Order


@csrf_exempt
@require_http_methods(["POST"])
def create_order(request: HttpRequest):
    data = json.loads(request.body.decode("utf-8"))

    customer, created = Customer.objects.get_or_create(email=data.get("email"))
    order = Order.objects.create(
        customer=customer, robot_serial=data.get("robot_serial")
    )

    return JsonResponse({"message": f"Заказ успешно создан! Номер заказа - {order.pk}"})
