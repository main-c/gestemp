from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="API de Gestion des Emploi du Temps",
        default_version="version 1",
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="edghimakoll@gmail"),
        license=openapi.License(name="BSD License"),
    ),
)

urlpatterns = [
    path("", include(("gestion.api_urls"))),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
