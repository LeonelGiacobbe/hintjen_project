from rest_framework import generics
from .models import Device
from .device_serializers import DeviceSerializer, DeviceUpdateSerializer

# ListCreateAPIView handles GET and POST requests for Device objects
class DeviceListCreateAPIView(generics.ListCreateAPIView):
    # state we're working with the Device model
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

# RetrieveUpdateAPIView handles GET and PATCH/ PUT requests for a single device
class DeviceRetrieveUpdateStatusAPIView(generics.RetrieveUpdateAPIView):
    queryset = Device.objects.all()
    
    # Choose between overall or PATCH/ PUT serializer
    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'PUT']:
            return DeviceUpdateSerializer
        return DeviceSerializer
