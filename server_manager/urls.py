from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Used for health check
def api_root(request):
     return JsonResponse({"status": "ok"})

urlpatterns = [
    path('api/', api_root),
    path('admin/', admin.site.urls),
    # Add Servers and Devices base urls
    path('api/servers/', include('api.server_urls')),
    path('api/devices/', include('api.device_urls')),
]
