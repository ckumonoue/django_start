from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("terms/", views.terms, name="terms"),
    path("api/info/", views.info, name="info"),
    path("admin-panel/", views.forbidden, name="forbidden"),
]
