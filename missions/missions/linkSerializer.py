from rest_framework import serializers

class RelatedClientSerializer(serializers.Serializer):
    '''
        Relationship Serializer pour le model Client
    '''
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(read_only=True)
    prenom = serializers.CharField(read_only=True)
    date_creation = serializers.DateTimeField(read_only=True)
    telephone =  serializers.CharField(read_only=True)

class RelatedProduitsSerializer(serializers.Serializer):
    '''
        Relationship Serializer pour le model Produit
    '''
    id = serializers.IntegerField(read_only=True)
    ville_depart=serializers.CharField(read_only=True)
    ville_arrivee=serializers.CharField(read_only=True)
    date_creation=serializers.DateTimeField(read_only=True)

class RelatedCategorieVehiculesSerializer(serializers.Serializer):
    '''
        Relationship Serializer pour le model Categorie
    '''
    id = serializers.IntegerField(read_only=True)
    intitule = serializers.CharField(read_only=True)
    date_creation=serializers.DateTimeField(read_only=True)

class RelatedTrajetsSerializer(serializers.Serializer):
    '''
        Relationship Serializer pour les trajets
    '''
    id = serializers.IntegerField(read_only=True)
    ville_depart=serializers.CharField(read_only=True)
    ville_arrivee=serializers.CharField(read_only=True)
    date_creation=serializers.DateTimeField(read_only=True)

class RelatedVehiculesSerializer(serializers.Serializer):
    '''
        Relationship Serializer pour tous les vehicules
    '''
    id = serializers.IntegerField(read_only=True)
    immat = serializers.CharField(read_only=True)
    marque = serializers.CharField(read_only=True)
    couleur= serializers.CharField(read_only=True)
    est_disponible = serializers.BooleanField(read_only=True)
    poids_vide = serializers.DecimalField(read_only=True,  max_digits=6, decimal_places=2 )

class RelatedChauffeursSerializer(serializers.Serializer):
    '''
        Relationship Serializer pour tous les vehicules
    '''
    nom= serializers.CharField(read_only=True)
    prenom= serializers.CharField(read_only=True)
   