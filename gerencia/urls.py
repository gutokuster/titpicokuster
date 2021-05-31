from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('itens/', views.listar_itens, name='listar_itens'),
    path('itens/cadastro', views.cadastrar_item, name='cadastrar_item'),
    path('itens/excluir/<int:pk>', views.excluir_item, name='excluir_item'),
    path('itens/atualizar/<int:pk>', views.atualizar_item, name='atualizar_item'),
]
