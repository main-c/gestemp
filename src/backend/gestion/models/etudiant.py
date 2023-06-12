from django.db import models
from django.contrib.auth.models import User

from .classe import Classe
from .groupe import Groupe


class Etudiant(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField(
        max_length=10, unique=True, null=False, editable=False
    )
    classe = models.ForeignKey(
        Classe, on_delete=models.SET_DEFAULT, default="None"
    )
    groupe = models.ForeignKey(Groupe, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"

    def __str__(self):
        return self.matricule
