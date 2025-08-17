from django.urls import path
from .server_views import ServerListCreateAPIView, ServerRetrieveUpdateStatusAPIView

urlpatterns = [
    path('', ServerListCreateAPIView.as_view(), name='server-list-create'),
    path('<int:pk>/', ServerRetrieveUpdateStatusAPIView.as_view(), name="server-detail"),
]
