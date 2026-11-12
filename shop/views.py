from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Strona główna sklepu django_start")


def about(request):
    return HttpResponse("Jesteśmy klasą 4TP. Robimy sklep internetowy.")


def contact(request):
    return HttpResponse("Kontakt: sklep@example.com, tel. 123 456 789")


def terms(request):
    return HttpResponse("Regulamin sklepu: zamówienia realizujemy w 2 dni robocze.")


def info(request):
    return JsonResponse({"name": "django_start", "author": "ckumonoue", "version": "0.1"})


def forbidden(request):
    return HttpResponse("Brak dostępu", status=403)


def hello(request, name):
    return HttpResponse(f"Cześć, {name}!")


def hello_age(request, name, age):
    return HttpResponse(f"Cześć, {name}! Masz {age} lat.")


def add(request, a, b):
    return HttpResponse(f"{a} + {b} = {a + b}")


def subtract(request, a, b):
    return HttpResponse(f"{a} - {b} = {a - b}")


def multiply(request, a, b):
    return HttpResponse(f"{a} * {b} = {a * b}")


def divide(request, a, b):
    if b == 0:
        return HttpResponse("Nie dzielimy przez zero", status=400)
    return HttpResponse(f"{a} / {b} = {a / b}")


def product_slug(request, slug):
    return HttpResponse(f"Produkt: {slug}")
