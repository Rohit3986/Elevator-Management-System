
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
   openapi.Info(
      title="ELEVATOR MANAGEMENT SYSTEM",
      default_version='v1',
      description="Your API description",
      terms_of_service="https://www.yourapp.com/terms/",
      contact=openapi.Contact(email="contact@yourapp.com"),
      license=openapi.License(name="Your License"),
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)

# schema_view = get_swagger_view(title='Your API')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('myapp.api.urls')),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui')
]
