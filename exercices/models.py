
from django.db import models
from django.contrib.auth.models import User
from .validators import no_TwoExercices

class Exercices(models.Model):
    date_exercice = models.DateTimeField(validators=[no_TwoExercices])
    etat_exercice = models.BooleanField(default=False)
    createur = models.ForeignKey(
     User , related_name='liste_exercices', 
     on_delete=models.SET_NULL, null=True
    )

    class Meta:
        ordering = ['-date_exercice']
    
    def __str__(self) -> str:
        return f' Exercice {self.date_exercice.year}'
    
    @property
    def nbreMissions(self):
        # for watch in my_user.watch_set.select_related('movie'):
        #     print(f'{watch.movie.title}: {watch.watched}, {watch.finished}')

        result = self.liste_missions.values('liste_depenses')

        for el in result :
            print(el)

        return f"{self.liste_missions.all().values('liste_depenses')}"
    
    @property
    def totalDepenseMaintenances(self):
        return self.maintenances.all().aggregate(models.Sum('montant'))['montant__sum']

    @property
    def totalDepenseMission(self):
        '''
            'montant__sum' : alias par defaut pour nommer l'attribut de l'aggregation
        '''
        return self.infoDepenseMission.all().aggregate(models.Sum('montant'))['montant__sum']

    @property
    def recetteTotales(self):
        '''
            l'aggregation(min, max, avg, std, ...) s'applique au attribut 
            du model: --> methode pour faire d'autre operation avec : Somme des 
            produits.
            utilisation de models.F() qui permet d'appliquer des operations sur le 
            champs des models
        '''
        return self.infoRecetteMission.all().aggregate(
           total= models.Sum(models.F('cout_unitaire')* models.F('qte_produit'))
            )['total']