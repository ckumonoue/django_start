from django.http import HttpResponse


def index(request):
    return HttpResponse("django_start – Django, materiał 10")
