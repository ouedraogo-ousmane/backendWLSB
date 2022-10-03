from rest_framework import generics, permissions
from rest_framework.response import Response
import rest_framework.status as status
from .serializers import (
    ClientSerializer, ProduitsSerializer, StatistiqueParDepensesSerializer, StatistiqueVehiculesParc,
    VehiculeParcsSerializer, LoueurVehiculesSerializer, chauffeurVehiculeMissionSerializer,
    documentVehiculesSerializer, CategorieVehiculesSerializer,
    RecetteDetailPesageSerializer, RecetteDetailSansPesageSerializer,
    MissionsSerializer,InfoDepenseMissionsSerializer,ChauffeursSerializer,
    VehiculesSerializer,TrajetsSerializer, VehiculeLouesSerializer,RecetteGlobleSerializer,
     DepenseMissionsSerializer, listAcceuilMissionExerciceSerializer)

from .models import (
    Clients, Produits, VehiculeParcs, VehiculeLoues,
    CategorieVehicules, documentVehicules, Trajets,
    RecetteDetailPesage, RecetteDetailSansPesage,
    Chauffeurs, Missions, LoueurVehicules,
    DepenseMissions, InfoDepenseMissions, Vehicules, Recettes)

class ClientListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post clients
    '''
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    paginator = None

list_create_clientAPIVIEW = ClientListCreateAPIView.as_view()


class RetUpdateDelClients(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des clients 
    '''
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_ClientsView = RetUpdateDelClients.as_view()


class ProduitsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post produits
    '''
    queryset = Produits.objects.all()
    serializer_class = ProduitsSerializer
    permission_classes = [permissions.IsAdminUser]
    paginator = None
list_create_ProduitsAPIVIEW = ProduitsListCreateAPIView.as_view()

class RetUpdateDelProduits(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des produits 
    '''
    queryset = Produits.objects.all()
    serializer_class = ProduitsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_ProduitsView = RetUpdateDelProduits.as_view()


class TrajetsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post Trajets
    '''
    queryset = Trajets.objects.all()
    serializer_class = TrajetsSerializer
    permission_classes = [permissions.IsAdminUser]
    paginator=None
list_create_TrajetsAPIVIEW = TrajetsListCreateAPIView.as_view()

class RetUpdateDelTrajets(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des Trajets 
    '''
    queryset = Trajets.objects.all()
    serializer_class = TrajetsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_TrajetsView = RetUpdateDelTrajets.as_view()

class CategorieVehiculesListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post CategorieVehicules
    '''
    queryset = CategorieVehicules.objects.all()
    serializer_class = CategorieVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_CategorieVehiculesAPIVIEW = CategorieVehiculesListCreateAPIView.as_view()

class RetUpdateDelCategorieVehicules(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des CategorieVehicules 
    '''
    queryset = CategorieVehicules.objects.all()
    serializer_class = CategorieVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_CategorieVehiculesView = RetUpdateDelCategorieVehicules.as_view()

class VehiculeParcsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post VehiculeParcs
    '''
    queryset = VehiculeParcs.objects.all()
    serializer_class = VehiculeParcsSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_VehiculeParcsAPIVIEW = VehiculeParcsListCreateAPIView.as_view()

class RetUpdateDelVehiculeParcs(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des VehiculeParcs 
    '''
    queryset = VehiculeParcs.objects.all()
    serializer_class = VehiculeParcsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_VehiculeParcsView = RetUpdateDelVehiculeParcs.as_view()

class VehiculeLouesListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post VehiculeLoues
    '''
    queryset = VehiculeLoues.objects.all()
    serializer_class = VehiculeLouesSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_VehiculeLouesAPIVIEW = VehiculeLouesListCreateAPIView.as_view()

class RetUpdateDelVehiculeLoues(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des VehiculeLoues 
    '''
    queryset = VehiculeLoues.objects.all()
    serializer_class = VehiculeLouesSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_VehiculeLouesView = RetUpdateDelVehiculeLoues.as_view()

class ChauffeursListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post Chauffeurs
    '''
    queryset = Chauffeurs.objects.all()
    serializer_class = ChauffeursSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_ChauffeursAPIVIEW = ChauffeursListCreateAPIView.as_view()

class RetUpdateDelChauffeurs(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des Chauffeurs 
    '''
    queryset = Chauffeurs.objects.all()
    serializer_class = ChauffeursSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_ChauffeursView = RetUpdateDelChauffeurs.as_view()

# nouveau
class RecetteDetailPesageListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post RecetteDetailPesage
    '''
    serializer_class = RecetteDetailPesageSerializer
    paginator = None
    
    def get_queryset(self):
        queryset = RecetteDetailPesage.objects.all()

        id_mission = self.request.query_params.get("id_mission")

        if id_mission is not None :
            queryset = queryset.filter(id_mission=id_mission)
        
            return queryset
        return None
    
    # def post(self, request, *args, **kwargs):
    #     print(request.data)
    #     serializer = RecetteDetailPesageSerializer(data=request.data, many=True)

    #     if serializer.is_valid(raise_exception=True):
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #     return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

list_create_RecetteDetailPesageAPIVIEW = RecetteDetailPesageListCreateAPIView.as_view()

class RetUpdateDelRecetteDetailPesage(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des RecetteDetailPesage 
    '''
    queryset = RecetteDetailPesage.objects.all()
    serializer_class = RecetteDetailPesageSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_RecetteDetailPesageView = RetUpdateDelRecetteDetailPesage.as_view()

# nouveau 
from datetime import datetime
from dateutil.relativedelta import relativedelta # module d'ajout de nbre sur une date.. (timedelta)
class documentVehiculesListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post documentVehicules
    '''
    serializer_class = documentVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
        
    def get_queryset(self):
        '''
            recuperation uniquement des documents dont la date d'expiration est 
            inferieur à 3 mois (date_exp.mois - today.mois <= 3)
        '''
        queryset = documentVehicules.objects.all()

        queryset = queryset.filter(date_expiration__month__lte=datetime.now().month+3,date_expiration__year= datetime.now().year)

        return queryset
    
list_create_documentVehiculesAPIVIEW = documentVehiculesListCreateAPIView.as_view()

class RetUpdateDeldocumentVehicules(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des documentVehicules 
    '''
    queryset = documentVehicules.objects.all()
    serializer_class = documentVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_documentVehiculesView = RetUpdateDeldocumentVehicules.as_view()

class RecetteDetailSansPesageListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post RecetteDetailSansPesage
    '''
    queryset = RecetteDetailSansPesage.objects.all()
    serializer_class = RecetteDetailSansPesageSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = RecetteDetailSansPesageSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

list_create_RecetteDetailSansPesageAPIVIEW = RecetteDetailSansPesageListCreateAPIView.as_view()

class RetUpdateDelRecetteDetailSansPesage(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des RecetteDetailSansPesage 
    '''
    queryset = RecetteDetailSansPesage.objects.all()
    serializer_class = RecetteDetailSansPesageSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_RecetteDetailSansPesageView = RetUpdateDelRecetteDetailSansPesage.as_view()


class MissionsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post Missions
    '''
    queryset = Missions.objects.all()
    serializer_class = MissionsSerializer
    permission_classes = [permissions.IsAdminUser]

list_create_MissionsAPIVIEW = MissionsListCreateAPIView.as_view()

class RetUpdateDelMissions(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des Missions 
    '''
    queryset = Missions.objects.all()
    serializer_class = MissionsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_MissionsView = RetUpdateDelMissions.as_view()


class DepenseMissionsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post DepenseMissions
    '''
    queryset = DepenseMissions.objects.all()
    serializer_class = DepenseMissionsSerializer
    permission_classes = [permissions.IsAdminUser]
    paginator = None
list_create_DepenseMissionsAPIVIEW = DepenseMissionsListCreateAPIView.as_view()

class RetUpdateDelDepenseMissions(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des DepenseMissions 
    '''
    queryset = DepenseMissions.objects.all()
    serializer_class = DepenseMissionsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_DepenseMissionsView = RetUpdateDelDepenseMissions.as_view()

class LoueurVehiculesListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post LoueurVehicules
    '''
    queryset = LoueurVehicules.objects.all()
    serializer_class = LoueurVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
list_create_LoueurVehiculesAPIVIEW = LoueurVehiculesListCreateAPIView.as_view()

class RetUpdateDeLoueurVehicules(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des LoueurVehicules 
    '''
    queryset = LoueurVehicules.objects.all()
    serializer_class = LoueurVehiculesSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_LoueurVehiculesView = RetUpdateDeLoueurVehicules.as_view()


class InfoDepenseMissionsListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post InfoDepenseMissions
    '''
    queryset = InfoDepenseMissions.objects.all()
    serializer_class = InfoDepenseMissionsSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = InfoDepenseMissionsSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

list_create_InfoDepenseMissionsAPIVIEW = InfoDepenseMissionsListCreateAPIView.as_view()

class RetUpdateDeInfoDepenseMissions(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des InfoDepenseMissions 
    '''
    queryset = InfoDepenseMissions.objects.all()
    serializer_class = InfoDepenseMissionsSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_InfoDepenseMissionsView = RetUpdateDeInfoDepenseMissions.as_view()

# vue personnalise 
class ListAcceuilMissionView(generics.ListAPIView):
    serializer_class = listAcceuilMissionExerciceSerializer

    def get_queryset(self):
        queryset = Missions.objects.all()

        id_exercice = self.request.query_params.get("exercice")
       
        if id_exercice is not None :
            queryset = queryset.filter(exercice_conerne__in=id_exercice)
            return queryset
        return None
listeAcceuilMissionsView = ListAcceuilMissionView.as_view()

class ListVehiculeProgrammerMission(generics.ListAPIView):
    queryset = VehiculeParcs.objects.all()
    serializer_class = chauffeurVehiculeMissionSerializer
    permission_classes = [permissions.IsAdminUser]
    paginator = None

listVehiculeProgrammerMissionView = ListVehiculeProgrammerMission.as_view()


class StatistiqueVehiculeParc(generics.ListAPIView):
    queryset = VehiculeParcs.objects.all()
    serializer_class = StatistiqueVehiculesParc
    permission_classes = [permissions.IsAdminUser]

infos_finance_vehicule_parc = StatistiqueVehiculeParc.as_view()


class StatistiqueParTypeDepenses(generics.ListAPIView):
    queryset = DepenseMissions.objects.all()
    serializer_class = StatistiqueParDepensesSerializer
    permission_classes = [permissions.IsAdminUser]
    paginator = None
info_finance_par_type_depense = StatistiqueParTypeDepenses.as_view()


class RecetteGlobalListCreateAPIView(generics.ListCreateAPIView):
    '''
        View: get, post Recette Global
    '''
    queryset = Recettes.objects.all()
    serializer_class = RecetteGlobleSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = RecetteGlobleSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
list_create_RecetteGlobalAPIVIEW = RecetteGlobalListCreateAPIView.as_view()


class RetUpdateDelRecetteGlobal(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des RecetteGlobal 
    '''
    queryset = Recettes.objects.all()
    serializer_class = RecetteGlobleSerializer
    permission_classes = [permissions.IsAdminUser]

ret_upate_del_RecetteRecetteGlobalDetailView = RetUpdateDelRecetteGlobal.as_view()

