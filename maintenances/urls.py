
from django.urls import path
from .views import (
    ret_update_del_MaintenanceView,
    list_create_MaintenanceView, ret_update_del_InfosPieceView,
    list_create_PiecesEchangesView, list_create_InfosPieceView,
    ret_update_del_PiecesEchangesView)
    
urlpatterns = [
    path('', list_create_MaintenanceView, name="listeCreerMaintenance"),
    path('<int:pk>/detail', ret_update_del_MaintenanceView, name="RetUpdateDelMaintenance"),

    path('pieces/', list_create_PiecesEchangesView, name="listeCreerPieces"),
    path('pieces/<int:pk>/detail', ret_update_del_PiecesEchangesView, name="RetUpdateDelPieces"),

    path('coutPieces/', list_create_InfosPieceView, name="listeCreercoutPieces"),
    path('coutPieces/<int:pk>/detail', ret_update_del_InfosPieceView, name="RetUpdateDelcoutPieces"),
]