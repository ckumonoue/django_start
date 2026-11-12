from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse

ITEMS = {
    1: "Laptop",
    2: "Mysz",
    3: "Klawiatura",
    4: "Monitor",
    5: "Słuchawki",
}


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


def items(request):
    category = request.GET.get("category", "all")
    sort = request.GET.get("sort", "default")
    page_raw = request.GET.get("page", "1")
    if not page_raw.isdigit():
        return HttpResponse("Parametr page musi być liczbą całkowitą", status=400)
    page = int(page_raw)
    return HttpResponse(f"Kategoria: {category}, sortowanie: {sort}, strona: {page}")


def item_detail(request, item_id):
    if item_id not in ITEMS:
        raise Http404("Nie ma takiego przedmiotu")
    return HttpResponse(f"Przedmiot: {ITEMS[item_id]}")


def start(request):
    return redirect("shop:index")


def links(request):
    lines = [
        reverse("shop:about"),
        reverse("shop:hello", args=["Ania"]),
        reverse("shop:item_detail", args=[3]),
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")
