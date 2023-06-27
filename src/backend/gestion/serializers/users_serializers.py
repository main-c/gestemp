from rest_framework import serializers
from gestion.models.user import User
from gestion.models.responsable import Enseignant


class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_teacher",
            "is_student",
            "is_responsable",
            "joined_at"
        )


class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = ("id", "user", "grade", "entite")


class EnseignantDetailSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer()

    class Meta:
        model = Enseignant
        fields = ("id", "user", "grade", "entite")
