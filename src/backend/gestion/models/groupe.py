from django.db import models

from .classe import Classe


class Groupe(models.Model):
    nom = models.CharField(max_length=255, null=False)
    capacite = models.IntegerField(null=False)
    code = models.CharField(max_length=10, unique=True, null=False)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Groupe"
        verbose_name_plural = "Groupes"

    def __str__(self):
        return self.code
