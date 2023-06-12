from django.db.models import Q
from rest_framework import serializers

# from gestion.models.administrateur import Administrateur
# from gestion.models.cours import Cours
# from gestion.models.groupe import Groupe
# from gestion.models.salle import Salle
# from gestion.models.responsable import Enseignant
from gestion.models.programmation import Programmation


class SerializerProgrammerCours(serializers.ModelSerializer):
    class Meta:
        model = Programmation
        fields = (
            "id",
            "enseignant",
            "groupe",
            "cours",
            "salle",
            "date",
            "debut",
            "fin",
            "cree_par",
        )

    def validate(self, attrs):
        # try:
        #     enseignant = Enseignant.objects.get(id=attrs["enseignant"].id)
        # except Enseignant.DoesNotExist:
        #     raise serializers.ValidationError("L'enseignant n'existe pas")

        # try:
        #     groupe = Groupe.objects.get(id=attrs["groupe"].id)
        # except Groupe.DoesNotExist:
        #     raise serializers.ValidationError("Le groupe n'existe pas")

        # try:
        #     cours = Cours.objects.get(id=attrs["cours"].id)
        # except Cours.DoesNotExist:
        #     raise serializers.ValidationError("Le cours n'existe pas")

        # try:
        #     salle = Salle.objects.get(id=attrs["salle"].id)
        # except Salle.DoesNotExist:
        #     raise serializers.ValidationError("La salle n'existe pas")

        # try:
        #     admin = Administrateur.objects.get(id=attrs["cree_par"].id)
        # except Administrateur.DoesNotExist:
        #     raise serializers.ValidationError("L'administrateur n'existe pas")

        if attrs["debut"] >= attrs["fin"]:
            raise serializers.ValidationError(
                "L'heure de début doit être inférieure à l'heure de fin"
            )

        # TEST 1: On vérifie que le professeur n'a pas déjà un cours à cette plage
        teste_1 = Programmation.objects.filter(
            Q(debut__lte=attrs["debut"]) & Q(fin__gte=attrs["debut"])
            | Q(debut__lte=attrs["fin"]) & Q(fin__gte=attrs["fin"]),
            enseignant=attrs["enseignant"],
            date=attrs["date"],
        )
        if teste_1.exists():
            raise serializers.ValidationError(
                "Le professeur a déjà un cours à cette plage"
            )

        # TEST 2: On vérifie que le groupe n'a pas déjà un cours à cette plage
        test_2 = Programmation.objects.filter(
            Q(debut__lte=attrs["debut"]) & Q(fin__gte=attrs["debut"])
            | Q(debut__lte=attrs["fin"]) & Q(fin__gte=attrs["fin"]),
            groupe=attrs["groupe"],
            date=attrs["date"],
        )
        if test_2.exists():
            raise serializers.ValidationError(
                "Le groupe a déjà un cours à cette plage"
            )

        # TEST 3: On vérifie que la salle n'a pas déjà un cours à cette plage
        test_3 = Programmation.objects.filter(
            Q(debut__lte=attrs["debut"]) & Q(fin__gte=attrs["debut"])
            | Q(debut__lte=attrs["fin"]) & Q(fin__gte=attrs["fin"]),
            salle=attrs["salle"],
            date=attrs["date"],
        )
        if test_3.exists():
            raise serializers.ValidationError(
                "La salle a déjà un cours à cette plage"
            )

        # TEST 4: On vérifie que la salle peut accueillir le groupe
        if attrs["salle"].capacite < attrs["groupe"].capacite:
            raise serializers.ValidationError(
                "La salle ne peut pas accueillir le groupe"
            )

        return attrs
