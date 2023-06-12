from django.urls import include, path
from rest_framework.routers import DefaultRouter

from gestion.views.programmer_cours import ViewSetProgrammerCours


router = DefaultRouter()
router.register("programmations", ViewSetProgrammerCours, basename="programmations")

urlpatterns = [
    path("", include(router.urls)),
]
