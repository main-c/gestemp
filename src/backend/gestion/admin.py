from django.contrib import admin

from gestion.models.administrateur import Administrateur
from gestion.models.classe import Classe, Filiere, Niveau
from gestion.models.cours import Cours
from gestion.models.etudiant import Etudiant
from gestion.models.groupe import Groupe
from gestion.models.programmation import Programmation
from gestion.models.responsable import Enseignant, Responsable
from gestion.models.salle import Salle


admin.site.site_header = (
    "Administration de l'application Gestion des Emploi du Temps"
)
admin.site.site_title = "Gestion des Emploi du Temps"
admin.site.index_title = (
    "Administration de l'application Gestion des Emploi du Temps"
)

admin.site.register(Administrateur)
admin.site.register(Classe)
admin.site.register(Niveau)
admin.site.register(Filiere)
admin.site.register(Cours)
admin.site.register(Etudiant)
admin.site.register(Groupe)
admin.site.register(Programmation)
admin.site.register(Responsable)
admin.site.register(Enseignant)
admin.site.register(Salle)
