from django.urls import path
from .device_views import DeviceListCreateAPIView, DeviceRetrieveUpdateStatusAPIView

urlpatterns = [
    path('', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    path('<int:pk>/', DeviceRetrieveUpdateStatusAPIView.as_view(), name="device-detail"),
]
