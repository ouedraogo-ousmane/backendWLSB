from django.db import models
from exercices.models import Exercices 
from missions.models import VehiculeParcs

class PiecesEchanges(models.Model):
    '''
        model : liste des pieces echangees
    '''
    nom = models.CharField(max_length=250, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['nom','-date_creation']

    def __str__(self):
        return self.nom

    
class Mantenances(models.Model):
    '''
        model pour les maintenances
    '''
    motif = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_maintenance = models.DateTimeField()
    montant = models.DecimalField(max_digits=19, decimal_places=5)

    exerciceConcerne =  models.ForeignKey(Exercices, related_name='maintenances', on_delete=models.CASCADE)
    vehiculeConcerne = models.ForeignKey(VehiculeParcs, related_name='maintenances_effectuees', on_delete=models.CASCADE)
    piecesEchangees = models.ManyToManyField(
        PiecesEchanges, through='InfosPieces', through_fields=('maintenanceConcernee', 'nomPiece'),
        ) # ne references un uniquement que l'id des pieces

    class Meta:
        ordering=['vehiculeConcerne','-date_creation']
    
    def __str__(self):
        return f"{self.vehiculeConcerne}"


class InfosPieces(models.Model): 
    '''
        model le cout des pieces et leur nombre
    '''
    coutUnitaire = models.DecimalField(max_digits=19, decimal_places=10)
    nombre = models.PositiveIntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)
    maintenanceConcernee = models.ForeignKey(Mantenances,related_name='pieces_enregistrees' ,on_delete=models.CASCADE)
    nomPiece = models.ForeignKey(PiecesEchanges, on_delete=models.CASCADE)

    class Meta:
        ordering=['maintenanceConcernee','-date_creation']
        constraints = [
            models.UniqueConstraint(
                fields=['maintenanceConcernee', 'nomPiece'],
                 name='unique_id_maint_piece')]


    def __str__(self):
        return f'{ self.maintenanceConcernee}'
    @property
    def prix_Achat(self):
        return f"{self.nombre * self.coutUnitaire}"