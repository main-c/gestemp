from django.urls import include, path
from rest_framework.routers import DefaultRouter

from gestion.views.programmer_cours import ViewSetProgrammerCours
from gestion.views import api_views

router = DefaultRouter()
router.register("plannings", ViewSetProgrammerCours, basename="programmations")
router.register("classes", api_views.ClasseViewSet, basename="classes")
router.register("filieres", api_views.FiliereViewSet, basename="filieres")
router.register("niveaux", api_views.NiveauViewSet, basename="niveaux")

router.register("salles", api_views.SalleViewSet, basename="salles")
router.register("teachers", api_views.EnseignantViewSet, basename="teachers")


urlpatterns = [
    path("", include(router.urls)),
]
