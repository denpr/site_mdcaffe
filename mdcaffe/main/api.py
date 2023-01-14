from .models import IncomingMessage
from rest_framework import viewsets, permissions
from .serializers import IncomingMessageSerializer

class IncomingMessageViewSet(viewsets.ModelViewSet):
    queryset = IncomingMessage.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IncomingMessageSerializer