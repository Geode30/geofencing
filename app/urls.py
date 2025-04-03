from django.urls import path
from app.views import check_in

urlpatterns = [
    path("geofencing/", check_in),
]