from rest_framework import generics
from .models import Server
from .server_serializers import ServerSerializer, ServerStatusUpdateSerializer


# ListCreateAPIView handles GET and POST requests for Server objects
class ServerListCreateAPIView(generics.ListCreateAPIView):
    # state we're working with the Server model
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

# RetrieveUpdateAPIView handles GET and PATCH/ PUT requests for a single server
class ServerRetrieveUpdateStatusAPIView(generics.RetrieveUpdateAPIView):
    queryset = Server.objects.all()
    
    # Choose between overall or PATCH/ PUT serializer
    def get_serializer_class(self):
        if self.request.method.lower() in ['patch', 'put']:
            return ServerStatusUpdateSerializer
        return ServerSerializer
