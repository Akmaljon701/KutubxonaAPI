from django.contrib import admin
from django.urls import path
from mainapp.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Kutubxona API",
      default_version='v1',
      description="Kutubxona boshqaruv tizimi uchun API",
      contact=openapi.Contact(email="akmaljonyoqubov088@gmail.com"),
      license=openapi.License(name="Akamljon Yoqubov"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin_panel/', admin.site.urls),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),

    path('mualliflar/', MualliflarAPIView.as_view()),
    path('muallif/<int:pk>/', MuallifDetailAPIView.as_view()),

    path('kitoblar/', KitoblarAPIView.as_view()),
    path('kitob/<int:pk>/', KitobDetailAPIView.as_view()),

    path('talabalar/', TalabalarAPIView.as_view()),
    path('talaba/<int:pk>/', TalabaDetailAPIView.as_view()),

    path('admin/', AdminlarAPIView.as_view()),
    path('adminlar/<int:pk>/', AdminDetailAPIView.as_view()),

    path('recordlar/', RecordlarAPIView.as_view()),
    path('record/<int:pk>/', RecordDetailAPIView.as_view()),
]
