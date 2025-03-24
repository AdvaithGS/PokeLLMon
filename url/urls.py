from django.urls import path

from . import views

urlpatterns = [
    path("", views.urlShort, name="index"),
    path("u/<str:slugs>", views.urlRedirect, name="redirect"),
    path("stats/", views.url_stats, name = "stats")
]
