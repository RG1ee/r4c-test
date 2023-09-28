import json
from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from src.apps.robots.forms import RobotForm


@csrf_exempt
@require_http_methods(["POST"])
def create_robot(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body.decode("utf-8"))
    form = RobotForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "Модель робота добавлена"})
    else:
        errors = form.errors.as_text()
        return JsonResponse({"errors": errors}, status=400)
