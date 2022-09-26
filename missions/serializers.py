from dataclasses import fields
from pickle import TRUE
from rest_framework import serializers

from .models import (
    Clients, Produits, VehiculeParcs, VehiculeLoues,
    CategorieVehicules, documentVehicules, Trajets,
    RecetteDetailPesage, RecetteDetailSansPesage,
    Chauffeurs, Missions, LoueurVehicules,Recettes,
    DepenseMissions, InfoDepenseMissions, Vehicules
    )

class ClientSerializer(serializers.ModelSerializer):
    '''
        Serializer du model client
    '''
    class Meta:
        model = Clients
        fields= ('id','nom', 'prenom')

class ProduitsSerializer(serializers.ModelSerializer):
    '''
        Serializer du model Produit
    '''
    class Meta:
        model = Produits
        fields= ('id', 'nom', 'unite')

class TrajetsSerializer(serializers.ModelSerializer):
    '''
        Serializer du model Produit
    '''
    intitule = serializers.SerializerMethodField()
    class Meta:
        model = Trajets
        fields= ('id', 'intitule','ville_depart','ville_arrivee')

    def get_intitule(self, obj):
        return f"{obj.ville_depart}-{obj.ville_arrivee}"

class CategorieVehiculesSerializer(serializers.ModelSerializer):
    '''
        Serializer du model des Categories de vehicule 
    '''
    class Meta:
        model = CategorieVehicules
        fields= '__all__'

class VehiculesSerializer(serializers.ModelSerializer):
    '''
        Serializer pour lestous les vehicules du parc
    '''

    class Meta:
        model = Vehicules
        fields = '__all__'

class documentVehiculesSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model documentVehicules
    '''
    class Meta:
        model = documentVehicules
        fields = '__all__'

class VehiculeParcsSerializer(VehiculesSerializer):
    # nbreDocument = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = VehiculeParcs
        fields = (
            'id',
            'immat',
            'marque' ,
            'couleur',
            # 'chauffeur'
            )

    # def get_nbreDocument(self, obj):
    #     return  obj.infos_documents.count()

class VehiculeLouesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculeLoues
        fields = '__all__'

class ChauffeursSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model chauffeurs
    '''
    class Meta:
        model = Chauffeurs
        fields = '__all__'

class RecetteDetailPesageSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model RecetteDetailPesage
    '''
    class Meta:
        model = RecetteDetailPesage
        fields = '__all__'

class RecetteDetailSansPesageSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model RecetteDetailSansPesage
    '''

    class Meta:
        model = RecetteDetailSansPesage
        fields = '__all__'


class RecetteGlobleSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model RecetteDetailSansPesage
    '''

    class Meta:
        model = Recettes
        fields = '__all__'

class DepenseMissionsSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model DepenseMissions
    '''
    class Meta:
        model = DepenseMissions
        fields =('id','intitule', 'montant')

class MissionsSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model Missions
    '''

    class Meta:
        model = Missions
        fields = '__all__'
        
class LoueurVehiculesSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model LoueurVehicules
    '''
    class Meta:
        model = LoueurVehicules
        fields = '__all__'

class InfoDepenseMissionsSerializer(serializers.ModelSerializer):
    '''
        Serializer pour le model InfoDepenseMissions
    '''
    class Meta:
        model = InfoDepenseMissions
        fields = '__all__'

# ----- serializer specifique concernant l'exercice ------

class listAcceuilMissionExerciceSerializer(serializers.ModelSerializer):
    
    chauffeur = serializers.SerializerMethodField()
    vehicule  = serializers.SerializerMethodField()
    depenses = serializers.SerializerMethodField()
    produits = serializers.SerializerMethodField()
    trajet =  serializers.SerializerMethodField()

    class Meta:
        model = Missions
        fields =(
            'id',
            'vehicule',
            'date_mission',
            'etat_mission',
            'motif',
            'chauffeur',
            'depenses',
            'produits',
            'trajet'
        )

    def get_trajet(self, obj):
        return Trajets.objects.filter(pk=obj.trajet_concerne_id).values('id','ville_depart', 'ville_arrivee')[0]

    def get_chauffeur(self, obj):
        return Chauffeurs.objects.filter(vehicule=obj.vehicule_concerne_id).values("id","nom", "prenom", "telephone")[0]

    def get_vehicule(self, obj):
        return Vehicules.objects.filter(pk=obj.vehicule_concerne_id).values("id","immat", "couleur", "marque", "poids_vide")[0]

    def get_depenses(self, obj):
        return obj.info_depenses.values("id","intitule_depense__id","intitule_depense__intitule","montant")

    def get_produits(self, obj):
        return obj.info_recette.values("id","client_concerne__id","client_concerne__nom", "client_concerne__prenom", "produit__id" ,"produit__nom", "produit__unite", "qte_produit") 

class chauffeurVehiculeMissionSerializer(serializers.ModelSerializer):
    chauff = serializers.SerializerMethodField()
    class Meta:
      model = VehiculeParcs
      fields = ('id','immat','chauff')

    def get_chauff(self, obj):
      '''
        retourner les informations 
        sur les chauffeurs du vehicules: nom, prenon
      '''
      return obj.chauffeur.values('nom', 'prenom')[0] # reourne une liste d'un element par vehicule

#Group.objects.filter(members=my_person_object)

from django.db.models import Sum, F

class StatistiqueVehiculesParc(serializers.ModelSerializer):
    total_depenses= serializers.SerializerMethodField()
    total_recette = serializers.SerializerMethodField()
    chauffeur =  serializers.SerializerMethodField()

    class Meta:
        model = VehiculeParcs
        fields = ('id', 'immat','chauffeur', 'total_depenses', 'total_recette')
    
    def get_total_depenses(self,obj):
        '''
            Calcul de les depenses total d'un vehicule en fonction d'un exercice
        '''

        request = self.context.get('request') # recuperation de meta donnee de la requete
        id_exercice = request.__dict__.get('parser_context').get('kwargs').get('pk')  # recuperation d'un parametre de l'url dans le serializer

        # recuperation des depenses mission du veh
        total= obj.liste_missions.filter(exercice_conerne_id=id_exercice
                    ).values('id').aggregate(resultat = Sum('info_depenses__montant'))['resultat']

        if total is None : total = 0 

        # recuperation des depenses maintenances du veh
        dep_maint  = obj.maintenances_effectuees.filter(exerciceConcerne = id_exercice ).values('montant')

        # calcul de la depense:  A ameliorer
        if dep_maint is not None :

            for value in dep_maint : # boucle obligatoire pour recuperer le montant à cause du type des donnees
                total += value['montant']

        return total 

    def get_total_recette(self,obj):
        '''
            Calcul de la recette d'un vehicule en fonction d'un exercice
        '''
        request = self.context.get('request')
        id_exercice = request.__dict__.get('parser_context').get('kwargs').get('pk')  # recuperation d'un parametre de l'url dans le serializer

        return obj.liste_missions.filter(exercice_conerne_id=id_exercice).values('id').aggregate(resultat=Sum(F('info_recette__cout_unitaire') * F('info_recette__qte_produit')))['resultat']

    def get_chauffeur(self, obj):
        '''
            Chauffeur du vehicule
        '''
        return Chauffeurs.objects.filter(vehicule=obj.id).values("nom", "prenom", "telephone")[0]


class StatistiqueParDepensesSerializer(serializers.ModelSerializer):
    
    montant = serializers.SerializerMethodField()

    class Meta:
        model = DepenseMissions
        fields= ('id', 'intitule', 'montant')
    
    def get_montant(self, obj):
        request = self.context.get('request') # recuperation de meta donnee de la requete
        id_exercice = request.__dict__.get('parser_context').get('kwargs').get('pk')  # recuperation d'un parametre de l'url dans le serializer
        
        return   obj.detail_cout.filter(exercice=id_exercice).values('montant').aggregate(result = Sum('montant'))['result']

