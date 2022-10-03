        # MODEL : PACKAGE MISSION

from asyncio import constants
from datetime import datetime
from django.db import models
import django.db.models.constraints as _
from django.contrib.auth.models import User
from exercices.models import Exercices

    # Create your models here.
class Clients(models.Model):
    '''
        tables contenant la liste des clients de l'entreprise 
        pour une mission
    '''
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    telephone =  models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['nom']

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Produits(models.Model):
    '''
        table contenant la liste des produits transportes
        dans une mission
    '''
    LISTE_UNTES = [
        ('Kg', 'kilogramme'),
        ('tonne','tonne'),
        ('tube', 'tube')
    ]

    nom = models.CharField(max_length=250)
    date_creation = models.DateTimeField(auto_now_add=True)
    unite = models.CharField(max_length=25, choices=LISTE_UNTES, default='Kg')

    class Meta:
        ordering = ['nom']

    def __str__(self):
        return self.nom

class Trajets(models.Model):
    '''
        tables contenant la liste des trajet 
        prise dans une mission
    '''
    LISTE_VILLES = [
        ('Ouaga', 'Ouagadougou'),
        ('Bobo', 'Bobo Dioulasso'),
        ('Bamako', 'Bamako'),
        ('Accra', 'Accra')
    ]

    ville_depart=models.CharField(max_length=50, choices=LISTE_VILLES, default='Bobo')
    ville_arrivee=models.CharField(max_length=50, choices=LISTE_VILLES, default='Bobo')
    date_creation=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_creation']
    
    def __str__(self) -> str:
        return f'{self.ville_depart }-{self.ville_arrivee}'

class CategorieVehicules(models.Model):
    '''
        tables contenant la liste des categorie de vehicule
    '''
    intitule = models.CharField(max_length=60, unique=True)
    date_creation=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['intitule', '-date_creation']
    
    def __str__(self) -> str:
        return self.intitule
    
class Vehicules(models.Model):
    '''
        table contenant la liste de tous les vehicules
    '''

    immat = models.CharField(max_length=250, unique=True)
    marque = models.CharField(max_length=60, null=True)
    couleur= models.CharField(max_length=60, null=True)
    est_disponible = models.BooleanField(default=True)
    poids_vide = models.DecimalField(max_digits=10, decimal_places=7)

    categorie = models.ForeignKey(
        CategorieVehicules,
        related_name='vehicules',
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        ordering = ['immat']
    
    def __str__(self) -> str:
        return self.immat

class VehiculeParcs(Vehicules):
    '''
        tables contenant la liste des vehicules du propre 
        au parc automobile
    '''
    
    @property
    def total_depenses_Mission(self):
        return None

    @property
    def total_Maintenance(self):
        return None

    @property
    def total_recette(self):
        return None

class Chauffeurs(models.Model):
    '''
        tables contenant la liste des chauffeurs
    '''
    nom= models.CharField(max_length=250)
    prenom= models.CharField(max_length=250)
    telephone=models.CharField(max_length=20)
    salaire= models.DecimalField(max_digits=19, decimal_places=10,default=0.0)
    #photo = models.ImageField()
    date_creation = models.DateTimeField(auto_now_add=True)

    vehicule=models.ForeignKey(
        VehiculeParcs,
        related_name='chauffeur',
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        ordering = ['nom', 'prenom']
    
    def __str__(self) -> str:
        return f"{self.nom} {self.prenom}"

class LoueurVehicules(models.Model):
    '''
        Table contanent la listes fournisseur de vehicule
    '''
    nom= models.CharField(max_length=250)
    prenom = models.CharField(max_length=250, null=True)
    telephone = models.CharField(max_length=20, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ['nom', 'prenom']
    
    def __str__(self):
        return f'{self.nom} - {self.prenom}'

class VehiculeLoues(Vehicules):
    '''
        tables des vehicule loues
    '''
    proprietaire = models.ForeignKey(
        LoueurVehicules,
        related_name='vehicules',
        on_delete=models.CASCADE
    )

class docsTransports(models.Model):
    '''
        tables contenant la liste de tous les vehicules de transport
    '''
    LISTE_DOCS = [ #nouveau
        ('visite technique','visite technique'),
        ('assurance', 'assurance')
    ]
    intitule = models.CharField(max_length=250, choices=LISTE_DOCS)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateField()

    class Meta:
        ordering = ['intitule']
    
    def __str__(self) -> str:
        return self.intitule

    @property
    def nbreJoursRestant(self):
        return f'{self.date_expiration.day - datetime.now().day} '
        
    @property
    def nbreMoisRestant(self):
        return f'{self.date_expiration.month - datetime.now().month} '

class documentVehicules(docsTransports):
    '''
        table contenant les informations sur la date d'expiration des documents
        d'un vehicule
    '''
    # LISTE_DOCS = [
    #     ('visite technique','visite technique'),
    #     ('assurance', 'assurance')
    # ]

    vehicule = models.ForeignKey(
        VehiculeParcs,
        related_name='infos_documents',
        on_delete=models.CASCADE
    )

class DepenseMissions(models.Model):
    '''
        tables contanant l'intitule des depenses
    '''
    LISTES_DEPENSES = [
        ('frais de carburant', 'frais de carburant'),
        ('frais de voyage', 'frais de voyage'),
        ('frais de douane', 'frais de douane'),
        ]
    date_creation = models.DateTimeField(auto_now_add=True)
    intitule = models.CharField(max_length=250 , choices=LISTES_DEPENSES , unique=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self) -> str:
        return self.intitule

    @property
    def montant(self):
        return self.detail_cout.all().aggregate(total=models.Sum('montant'))['total']


class Missions(models.Model):
    ''''
        tables contenant la liste des missions realisees
    '''

    LISTES_MOTIFS=[
        ('Approvissionement', 'Approvissionement'),
        ('Livraison', 'Livraison')]

    exercice_conerne = models.ForeignKey(
        Exercices,
        related_name='liste_missions',
        on_delete=models.CASCADE)

    vehicule_concerne = models.ForeignKey(
        Vehicules,
        related_name='liste_missions',
        on_delete=models.CASCADE)

    trajet_concerne = models.ForeignKey(
        Trajets,
        related_name='liste_missions',
        on_delete=models.SET_NULL, null=True)

    liste_produits = models.ManyToManyField(
        Produits,
        through='Recettes',
        through_fields=('mission','produit'), related_name='liste_produits')

    liste_depenses = models.ManyToManyField(
        DepenseMissions,
        through='InfoDepenseMissions',
        through_fields=('mission','intitule_depense'))

    date_mission = models.DateField()
    date_creation = models.DateTimeField(auto_now_add=True)
    etat_mission = models.BooleanField(default=False)
    motif = models.CharField(
        max_length=250,
        choices=LISTES_MOTIFS,
        default='Approvissionement')
    
    class Meta:
        ordering = ['-date_mission']

    def __str__(self) -> str:
        return f" mission du {self.date_mission}"

    @property
    def sommeDepenses(self):
        return self.info_depenses.values('montant','intitule_depense')
        # .aggregate(models.Sum('montant'))['montant__sum']

class InfoDepenseMissions(models.Model):
    ''''
        tables contenant le cout des depenses d'une mission
    '''
    intitule_depense = models.ForeignKey(
        DepenseMissions,
        related_name='detail_cout',
        on_delete=models.CASCADE)

    mission = models.ForeignKey(
        Missions,
        related_name='info_depenses',
        on_delete=models.CASCADE)

    montant = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    date_creation = models.DateTimeField(auto_now_add=True)

    # Denormalisation pour failite les requetes
    exercice = models.ForeignKey(
        Exercices,
        related_name='infoDepenseMission', 
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['intitule_depense']

    def __str__(self) -> str:
        return f'{self.intitule_depense}'

class Recettes(models.Model):
    ''''
        tables contenant la liste des produits, le client et 
        le montant generer par la mission
    '''
    produit = models.ForeignKey(
        Produits,
        related_name='info_recette',
        on_delete=models.CASCADE)

    mission = models.ForeignKey(
        Missions,
        related_name='info_recette', 
        on_delete=models.CASCADE)

    client_concerne = models.ForeignKey(
        Clients,
        related_name='info_recette', 
        on_delete=models.CASCADE)

    cout_unitaire = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    qte_produit = models.PositiveIntegerField(default=1)
    date_creation = models.DateTimeField(auto_now_add=True)

    exercice = models.ForeignKey(
    Exercices,
    related_name='infoRecetteMission', 
    on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_creation']
        constraints = [
            models.UniqueConstraint(fields=('produit', 'mission', 'client_concerne'), 
            name="unique_recette_key"),
        ]
        
    def __str__(self) -> str:
        return f"{self.mission}"

    @property
    def total(self):
        return ".2f"%(self.cout_unitaire * self.qte_produit )

class RecetteDetailSansPesage(models.Model):
    ''''
        tables contenant la liste des recettes dont le systeme de calcule 
        ne se base pas sur le poids des pesees
    '''
    id_recette = models.ForeignKey(Recettes, related_name="infos_snsPesee", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id_recette']

    def __str__(self) -> str:
        return f"{self.id_recette}"

# nouveau 
class RecetteDetailPesage(models.Model):
    '''
        tables contenant la liste des recettes dont le systeme de calcule 
        se base pas sur le poids des pesees
    '''

    id_mission = models.ForeignKey(Missions, related_name="infos_pesee", on_delete=models.CASCADE)
    premier_pese = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    deuxieme_pese = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_creation']

    def __str__(self) -> str:
        return f"{self.id_mission}"

    @property
    def poids_net(self):
        return ".2f"%(self.deuxieme_pese - self.premier_pese)
