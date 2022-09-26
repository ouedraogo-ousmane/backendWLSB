from rest_framework import generics, permissions
from .serializers import (
    InfoCoutSerializer, MantenanceSerializer, PiecesEchangeSerializer, 
    InfosPieceSerializer)
from .models import PiecesEchanges, Mantenances, InfosPieces

# maintenance

class ListCreateMantenancesView(generics.ListCreateAPIView):
    queryset = Mantenances.objects.all()
    serializer_class = MantenanceSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_MaintenanceView = ListCreateMantenancesView.as_view()

class RetUpdateDelMantenancesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mantenances.objects.all()
    serializer_class = MantenanceSerializer
    permission_classes = [permissions.IsAdminUser]
ret_update_del_MaintenanceView = RetUpdateDelMantenancesView.as_view()

# pieces

class ListCreatePiecesEchangesView(generics.ListCreateAPIView):
    queryset = PiecesEchanges.objects.all()
    serializer_class = PiecesEchangeSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_PiecesEchangesView = ListCreatePiecesEchangesView.as_view()

class RetUpdateDelPiecesEchangesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PiecesEchanges.objects.all()
    serializer_class = PiecesEchangeSerializer
    permission_classes = [permissions.IsAdminUser]
ret_update_del_PiecesEchangesView = RetUpdateDelPiecesEchangesView.as_view()

# cout des pieces

class ListCreateInfosPieceView(generics.ListCreateAPIView):
    queryset = InfosPieces.objects.all()
    serializer_class = InfoCoutSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_InfosPieceView = ListCreateInfosPieceView.as_view()

class RetUpdateDelInfosPieceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InfosPieces.objects.all()
    serializer_class = InfoCoutSerializer
    permission_classes = [permissions.IsAdminUser]
ret_update_del_InfosPieceView = RetUpdateDelInfosPieceView.as_view()