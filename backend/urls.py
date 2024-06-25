from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from backend import views

# versiones API

router = routers.DefaultRouter()
router.register(r'Responsable', views.ResponsableView, 'Responsable')
router.register(r'CentroCosto', views.CentroCostoView, 'CentroCosto')
router.register(r'AreaResponsabilidad', views.AreaResponsabilidadView, 'AreaResponsabilidad')
router.register(r'Sede', views.SedeView, 'Sede')
router.register(r'Edificio', views.EdificioView, 'Edificio')
router.register(r'Local', views.LocalView, 'Local')
router.register(r'Reservacion', views.ReservacionView, 'Reservacion')
router.register(r"Extras", views.Extras, "Extras")

urlpatterns = [
    path("api/", include(router.urls)),
    path('docs/', include_docs_urls(title="Locales API")),
]
