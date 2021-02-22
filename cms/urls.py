from django.contrib import admin
from django.db import router
from django.db.models import base
from django.urls import path, include
from artigo.views import ArtigoViewSet, CategoriaViewSet, ListaArtigoPublicadoAtivoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('artigos', ArtigoViewSet, basename='Artigos')
router.register('categorias', CategoriaViewSet, basename='Categorias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('artigos/ativo', ListaArtigoPublicadoAtivoViewSet.as_view())
]
