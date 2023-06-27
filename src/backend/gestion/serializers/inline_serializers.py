from django.db.models import Q
from rest_framework import serializers
from gestion.models.cours import Cours
from gestion.models.groupe import Groupe
from gestion.models.salle import Salle
from gestion.models.responsable import Enseignant
from gestion.models.classe import Classe, Niveau, Filiere


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = (
            'id',
            "titre",
            "code"
        )


class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = (
            'id',
            "titre",
            "code"
        )


class ClassDetailSerializer(serializers.ModelSerializer):
    filiere = FiliereSerializer()
    niveau = NiveauSerializer()

    class Meta:
        model = Classe
        fields = (
            'id',
            "name",
            "capacite",
            "code",
            "filiere",
            "niveau",
        )


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classe
        fields = (
            'id',
            "name",
            "capacite",
            "code",
            "filiere",
            "niveau",
        )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groupe
        fields = (
            'id',
            "nom",
            "capacite",
            "code",
            "classe",
        )


class GroupDetailSerializer(serializers.ModelSerializer):

    classe = ClassSerializer()

    class Meta:
        model = Groupe
        fields = (
            'id',
            "nom",
            "capacite",
            "code",
            "classe",
        )


class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = (
            'id',
            "designation",
            "capacite",
            "code"
        )
