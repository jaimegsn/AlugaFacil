from django.urls import path
from plataforma import views

urlpatterns = [
    path("home/", views.home, name="plataforma_urls-home"),
    path("cad_imovel/", views.cad_imoveis, name="plataforma_urls-cad_imovel"),
    path("announce/<int:id>/", views.announce,
         name="plataforma_urls-announce"),

    path("share_home/", views.share_home, name="plataforma_urls-share_home"),
    path("share_cad/", views.share_cad, name="plataforma_urls-share_cad"),
]
