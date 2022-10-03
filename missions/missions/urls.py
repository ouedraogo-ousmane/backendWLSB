from django.urls import path
from .views import(
    list_create_TrajetsAPIVIEW,ret_upate_del_TrajetsView,list_create_clientAPIVIEW, ret_upate_del_ClientsView,
    list_create_ProduitsAPIVIEW, ret_upate_del_ProduitsView,
    ret_upate_del_CategorieVehiculesView, list_create_CategorieVehiculesAPIVIEW,
    list_create_VehiculeParcsAPIVIEW, ret_upate_del_VehiculeParcsView,
    list_create_VehiculeLouesAPIVIEW, ret_upate_del_VehiculeLouesView,
    list_create_RecetteDetailPesageAPIVIEW, ret_upate_del_RecetteDetailPesageView,
    list_create_documentVehiculesAPIVIEW, ret_upate_del_documentVehiculesView,
    list_create_RecetteDetailSansPesageAPIVIEW, ret_upate_del_RecetteDetailSansPesageView,
    list_create_MissionsAPIVIEW, ret_upate_del_MissionsView,infos_finance_vehicule_parc, 
    list_create_DepenseMissionsAPIVIEW, ret_upate_del_DepenseMissionsView,
    list_create_LoueurVehiculesAPIVIEW, ret_upate_del_LoueurVehiculesView,
    list_create_InfoDepenseMissionsAPIVIEW, ret_upate_del_InfoDepenseMissionsView,
    listeAcceuilMissionsView, listVehiculeProgrammerMissionView,
    list_create_ChauffeursAPIVIEW,ret_upate_del_ChauffeursView, info_finance_par_type_depense,
    list_create_RecetteGlobalAPIVIEW, ret_upate_del_RecetteRecetteGlobalDetailView
    )

urlpatterns = [

    # URL: clients, produits, categorie vehicules
    path('Clients/', list_create_clientAPIVIEW, name="listerCreerClient"),
    path('Clients/<int:pk>/detail/', ret_upate_del_ClientsView, name="retUPDelClient"),

    path('produits/', list_create_ProduitsAPIVIEW, name="listerCreerProduits"),
    path('produits/<int:pk>/detail/', ret_upate_del_ProduitsView, name="retUPDelProduits"),
    
    path('categories/',list_create_CategorieVehiculesAPIVIEW , name="listerCreerCategorieVeh"),
    path('categories/<int:pk>/detail/', ret_upate_del_CategorieVehiculesView, name="retUPDelProduits"),
    
    # URL: Vehicule Parcs, recette avec pesage, vehicule louee
    path('vehiculeParcs/',list_create_VehiculeParcsAPIVIEW , name="listerCreerVehParcs"),
    path('vehiculeParcs/<int:pk>/detail/', ret_upate_del_VehiculeParcsView, name="retUPDelVehParcs"),

    path('recettePesees/',list_create_RecetteDetailPesageAPIVIEW , name="listerCreerRecettePesage"),
    path('recettePesees/<int:pk>/detail/', ret_upate_del_RecetteDetailPesageView, name="retUPDelRecettePesage"),

    path('vehiculeLoues/',list_create_VehiculeLouesAPIVIEW, name="listerCreervehiculeLoues"),
    path('vehiculeLoues/<int:pk>/detail/', ret_upate_del_VehiculeLouesView, name="retUPDelvehiculeLoues"),

    # URL: documents vehicules, recette sans pesage, missions
    path('docsVehicules/',list_create_documentVehiculesAPIVIEW, name="listerCreerdocsVehicules"),
    path('docsVehicules/<int:pk>/detail/', ret_upate_del_documentVehiculesView, name="retUPDeldocsVehicules"),

    path('recetteSansPesees/',list_create_RecetteDetailSansPesageAPIVIEW, name="listerCreerrecetteSansPesees"),
    path('recetteSansPesees/<int:pk>/detail/', ret_upate_del_RecetteDetailSansPesageView, name="retUPDelrecetteSansPesees"),
    
    path('recetteGlobale/',list_create_RecetteGlobalAPIVIEW, name="listerCreerrecetteSansPesees"),
    path('recetteGlobale/<int:pk>/detail/', ret_upate_del_RecetteRecetteGlobalDetailView, name="retUPDelrecetteSansPesees"),
    
    path('creer/',list_create_MissionsAPIVIEW, name="listerCreermissions"),
    path('<int:pk>/detail/', ret_upate_del_MissionsView, name="retUPDelmissions"),

    # URL:  fournisseur de vehicule, depenses missions
   
    path('depMissionName/',list_create_DepenseMissionsAPIVIEW, name="listerCreerdepensesMissions"),
    path('depMissionName/<int:pk>/detail/', ret_upate_del_DepenseMissionsView, name="retUPDeldepensesMissions"),
    path('depStatistique/<int:pk>/detail/', info_finance_par_type_depense, name="info_financeTypeDep"),

    path('LoueurVe  hicules/',list_create_LoueurVehiculesAPIVIEW, name="listerCreerLoueur"),
    path('LoueurVehicules/<int:pk>/detail/', ret_upate_del_LoueurVehiculesView, name="retUPDelLoueur"),
    path('info_finance/<int:pk>/detail/', infos_finance_vehicule_parc, name="infoFinanceVehicule"),

    path('depensesMissions/',list_create_InfoDepenseMissionsAPIVIEW, name="listerCreerLoueur"),
    path('depensesMissions/<int:pk>/detail/', ret_upate_del_InfoDepenseMissionsView, name="retUPDelLoueur"),

    # url personnalise
    path('acceuil/', listeAcceuilMissionsView, name="listeMissionAcceuil"),
    
    path('programmerVehicule/', listVehiculeProgrammerMissionView, name="listeChauffeurProgrammer"),

    path('trajetsList/', list_create_TrajetsAPIVIEW, name="trajetsList"),
    path('trajetsList/<int:pk>/detail/',ret_upate_del_TrajetsView, name="retUPDelLoueur"),

    path('chauffeurs/', list_create_ChauffeursAPIVIEW, name="chauffeurs"),
    path('chauffeurs/<int:pk>/detail/',ret_upate_del_ChauffeursView, name="chauffeurUpdating"),

]