from django.urls import re_path
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import Login, Logout

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación de API",
      default_version='v1',
      description="Documentación pública de API para Invera Challenge",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tomastessio@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path('usuarios/', include('users.urls')),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='login')
]
