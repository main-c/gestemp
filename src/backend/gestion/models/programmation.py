from django.db import models

from .groupe import Groupe
from .responsable import Enseignant
from .cours import Cours
from .salle import Salle
from .user import User


class Programmation(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    debut = models.TimeField(null=False)
    fin = models.TimeField(null=False)

    date_creation = models.DateTimeField(auto_now=True)
    date_modification = models.DateTimeField(auto_now_add=True)
    cree_par = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Programmation"
        verbose_name_plural = "Programmations"

    def __str__(self):
        return f"Programmation du {self.date} de {self.debut} - {self.fin}"
