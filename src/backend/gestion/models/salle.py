from django.db import models


class Salle(models.Model):
    designation = models.CharField(max_length=255, null=False)
    capacite = models.IntegerField(null=False)
    code = models.CharField(max_length=10, null=False)

    class Meta:
        verbose_name = "Salle"
        verbose_name_plural = "Salles"

    def __str__(self):
        return self.code
