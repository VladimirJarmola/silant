from django.urls import include, path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views import CarsViewSet, MaintenanceViewSet, ReclamationViewSet

app_name = "api"

router = routers.DefaultRouter()

router.register(r"cars", CarsViewSet)
router.register(r"maintenance", MaintenanceViewSet)
router.register(r"reclamation", ReclamationViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Silant API",
        default_version="v1.0.0",
        description="obtaining data from the tables Cars, Maintenance, Reclamation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += router.urls
