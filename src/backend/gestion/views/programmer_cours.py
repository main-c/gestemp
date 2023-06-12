from rest_framework import viewsets

from gestion.serializers.programmer_cours import SerializerProgrammerCours
from gestion.models.programmation import Programmation


class ViewSetProgrammerCours(viewsets.ModelViewSet):
    serializer_class = SerializerProgrammerCours
    queryset = Programmation.objects.all()
