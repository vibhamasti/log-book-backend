# django imports
from rest_framework import viewsets

# app level imports
from .serializers import LogBookSerializer
from .models import LogBook


class LogBookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing log book instances.
    """

    serializer_class = LogBookSerializer
    queryset = LogBook.objects.all()
