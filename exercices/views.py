from dataclasses import fields
from rest_framework import generics, permissions
from .models import Exercices
from .serializers import ExercicesFinanceInfoSerializer, ExercicesSerializer
#import rest_framework_filters as filters

from rest_framework import filters

    # Seul l'administrateur doit pouvoir effectuer ces actions

class ListCreateExecices(generics.ListCreateAPIView):
    '''
        View pour get, post des exercices 
    '''
    queryset = Exercices.objects.all()
    serializer_class = ExercicesSerializer
    permission_classes = [permissions.IsAdminUser]
    filterset_fields = ['date_exercice', 'etat_exercice'] 
    

    def perform_create(self, serializer):
        '''
            sauvegarder celui qui a creer l'exercice
        '''
        serializer.save(createur=self.request.user)
list_create_ExercicesView = ListCreateExecices.as_view()

class RetUpdateDelExercices(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des exercices 
    '''
    queryset = Exercices.objects.all()
    serializer_class = ExercicesFinanceInfoSerializer
    permission_classes = [permissions.IsAdminUser]

ret_upate_del_ExercicesView = RetUpdateDelExercices.as_view()


class ExercicesList(generics.ListAPIView):
    serializer_class = ExercicesSerializer

    def get_queryset(self):
        queryset = Exercices.objects.all()
        year = self.request.query_params.get('year')

        mois = self.request.query_params.get('mois')
        if year is not None :
            # Sample.objects.filter(date__year='2011', 
            #           date__month='01')
            queryset = queryset.filter(date_exercice__year=year, date_exercice__month=mois)

        return queryset

exo_test = ExercicesList.as_view()

class ListStatistiqueView(generics.ListCreateAPIView):
    queryset = Exercices.objects.all()
    serializer_class = ExercicesFinanceInfoSerializer
    permission_classes = [permissions.IsAdminUser]
list_StatView = ListStatistiqueView.as_view()
