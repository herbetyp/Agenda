from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:detalhes_id>', views.ver_detalhes, name='ver_detalhes'),
]

