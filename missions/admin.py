from django.contrib import admin
from .models import (
    Clients, Produits, VehiculeParcs, VehiculeLoues,
    CategorieVehicules, documentVehicules, Trajets,
    RecetteDetailPesage, RecetteDetailSansPesage,
    Chauffeurs, Missions, LoueurVehicules,
    DepenseMissions, InfoDepenseMissions, Recettes
    )

# Register your models here.

admin.site.register(Clients)
admin.site.register(Produits)
admin.site.register(VehiculeParcs)
admin.site.register(VehiculeLoues)
admin.site.register(documentVehicules)
admin.site.register(Trajets)
admin.site.register(RecetteDetailPesage)
admin.site.register(RecetteDetailSansPesage)
admin.site.register(Chauffeurs)
admin.site.register(Missions)
admin.site.register(CategorieVehicules)
admin.site.register(LoueurVehicules)
admin.site.register(DepenseMissions)
admin.site.register(InfoDepenseMissions)
admin.site.register(Recettes) # new 