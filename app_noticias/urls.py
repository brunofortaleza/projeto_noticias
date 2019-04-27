from django.urls import path
from . import views
from app_noticias.views import noticias_resumo_template, HomePageView, noticias_detalhes

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('noticias/resumo/', noticias_resumo_template, name = 'resumo'),
    path('noticias/<int:noticia_id>/', noticias_detalhes, name = 'detalhes')
]