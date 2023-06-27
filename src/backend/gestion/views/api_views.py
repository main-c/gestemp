from rest_framework import viewsets

from gestion.serializers.programmer_cours import SerializerProgrammerCours
from gestion.models.programmation import Programmation
from gestion.models.classe import Classe, Filiere, Niveau
from gestion.models.groupe import Groupe
from gestion.models.salle import Salle
from gestion.models.responsable import Enseignant, Responsable
from gestion.serializers.users_serializers import EnseignantSerializer, EnseignantDetailSerializer
from gestion.serializers.inline_serializers import FiliereSerializer, NiveauSerializer, ClassSerializer, GroupSerializer, SalleSerializer, GroupDetailSerializer, ClassDetailSerializer
from rest_framework.permissions import SAFE_METHODS

SAFE_ACTIONS = ['list', 'retrieve', 'get']


class FiliereViewSet(viewsets.ModelViewSet):
    serializer_class = FiliereSerializer
    queryset = Filiere.objects.all()


class NiveauViewSet(viewsets.ModelViewSet):
    serializer_class = NiveauSerializer
    queryset = Niveau.objects.all()


class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ClassDetailSerializer
        return ClassSerializer


class GroupeViewSet(viewsets.ModelViewSet):
    queryset = Groupe.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return GroupDetailSerializer
        return GroupSerializer


class EnseignantViewSet(viewsets.ModelViewSet):
    queryset = Enseignant.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return EnseignantDetailSerializer
        return EnseignantSerializer


class SalleViewSet(viewsets.ModelViewSet):
    serializer_class = SalleSerializer
    queryset = Salle.objects.all()
