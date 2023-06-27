from django.db import models
from gestion.models.user import User

from gestion.constant import GRADES_ENSEIGNANTS, GradeEnseignant


class Responsable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Entité ici designe l'entité pour laquelle il est responsable.
    entite = models.CharField(max_length=255, null=False, blank=True)

    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"
        abstract = True

    def __str__(self):
        return f"{self.utilisateur.first_name} {self.utilisateur.last_name}"


class Enseignant(Responsable):
    grade = models.CharField(
        max_length=255,
        choices=GRADES_ENSEIGNANTS,
        default=GradeEnseignant.DOCTEUR,
    )

    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"
