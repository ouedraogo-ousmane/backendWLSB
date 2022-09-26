# SERIALIZER Maintenance
from dataclasses import fields
from rest_framework import serializers

from missions.models import Chauffeurs
from .models import PiecesEchanges, Mantenances, InfosPieces

class PiecesEchangeSerializer(serializers.ModelSerializer):
    """
        serializer de la liste des pieces echanges
    """
    class Meta:
        model = PiecesEchanges
        fields = '__all__'


class RelatedPiecesEchangeSerializer(serializers.Serializer):
     nom = serializers.CharField(read_only=True)
     id = serializers.IntegerField(read_only=True)

class InfosPieceSerializer(serializers.ModelSerializer):
    nomPiece = RelatedPiecesEchangeSerializer(read_only=True)
    
    class Meta:
        model = InfosPieces
        fields = (
            'coutUnitaire',
            'nombre',
            'nomPiece'
        )

class MantenanceSerializer(serializers.ModelSerializer):
    '''
        Serializer pour l'activite des maintenance
    '''
    #pieces_enregistrees = InfosPieceSerializer(many=True)
    # pieces = PiecesEchangeSerializer(source='piecesEchangees',many=True) # uniquement lid des pieces si non
    chauffeur = serializers.SerializerMethodField()

    class Meta:
        model = Mantenances
        fields = (
            'id',
            'motif',
            'date_maintenance',
            'montant',
            'vehiculeConcerne',
            #'pieces_enregistrees',
            'chauffeur',
            'exerciceConcerne'
        )

    def get_chauffeur(self, obj):
        vehicule = obj.vehiculeConcerne
        chauffeur  = Chauffeurs.objects.filter(vehicule=vehicule)
        return chauffeur.values("nom", "prenom")

class InfoCoutSerializer(serializers.ModelSerializer):
    '''
        serializer pour les informations sur le cout 
        des pieces echanges lors d'une maintenance
    '''
    picece_nom = serializers.ReadOnlyField(source='nomPiece.nom') 
    maintenance_date = serializers.ReadOnlyField(source='maintenanceConcernee.date_creation')

    class Meta:
       model = InfosPieces 
       fields = (
        'picece_nom',
        'nomPiece',
        'coutUnitaire',
        'nombre',
        'date_creation',
        'maintenanceConcernee',
        'prix_Achat',
        "maintenance_date",
        )

