
from datetime import datetime
from django.core.exceptions import ValidationError

def no_TwoExercices(value):
    '''
        Empecher qu'il y ai 02 exercices la meme annee
    '''
    today_year = datetime.now().year
    if value.year == today_year:
        raise ValidationError('un exercice existe deja pour cette annee !')
