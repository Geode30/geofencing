from django.http import JsonResponse
from django.shortcuts import render
from geopy.distance import geodesic
from app.models import OfficeLocation

# Function to check if the user is within the geofence
def is_within_geofence(user_lat, user_long, office):
    office_location = (office.latitude, office.longitude)
    user_location = (user_lat, user_long)
    
    distance = geodesic(user_location, office_location).meters
    return distance <= office.radius_meters  # Returns True if inside

# View to handle check-in requests
def check_in(request):
    if request.method == 'POST':
        emp_no = request.POST.get('emp_no')
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        
        office = OfficeLocation.objects.first()  # Assuming one office for now

        if is_within_geofence(latitude, longitude, office):
            # Log attendance here
            return JsonResponse({"message": "Checked in successfully!"}, status=200)
        else:
            return JsonResponse({"message": "Outside office area!"}, status=403)
    else:
        return JsonResponse({"message": "Invalid request method!"}, status=400)
