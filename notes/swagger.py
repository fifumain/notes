from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Notes API",
        default_version="v1",
        description="Тестове завдання",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(
            email="pustovoitenkofilip@gmail.com",
        ),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
