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
