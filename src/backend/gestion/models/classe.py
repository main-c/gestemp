from django.db import models


class Filiere(models.Model):
    titre = models.CharField(max_length=255, null=False)
    code = models.CharField(max_length=10, unique=True, null=False)

    class Meta:
        verbose_name = "Filiere"
        verbose_name_plural = "Filieres"

    def __str__(self):
        return self.code


class Niveau(models.Model):
    titre = models.CharField(max_length=255, null=False)
    code = models.CharField(max_length=10, unique=True, null=False)

    class Meta:
        verbose_name = "Niveau"
        verbose_name_plural = "Niveaux"

    def __str__(self):
        return self.code


class Classe(models.Model):
    name = models.CharField(max_length=50, editable=False, null=False)
    capacite = models.IntegerField(null=False)
    code = models.CharField(
        max_length=10, editable=False, null=False, unique=True
    )
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.code
