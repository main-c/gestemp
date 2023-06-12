from django.db import models
from django.contrib.auth.models import User


class Administrateur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Administrateur"
        verbose_name_plural = "Administrateurs"

    def __str__(self):
        return f"{self.utilisateur.first_name} {self.utilisateur.last_name}"
