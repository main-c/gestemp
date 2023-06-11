from django.db import models


class Cours(models.Model):
    titre = models.CharField(max_length=255, null=False)
    code = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

    def __str__(self):
        return self.code
