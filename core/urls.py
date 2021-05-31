from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    # Buffet
    path('buffet/', views.buffet, name='buffet'),
    path('buffet/pedido/', views.criar_pedido, name='criar_pedido'),
    path('buffet/liberar_pedido/<int:pk>', views.liberar_pedido, name='liberar_pedido'),
    path('buffet/baixar_pedido/<int:pk>', views.baixar_pedido, name='baixar_pedido'),
    path('buffet/cancelar_pedido/', views.cancelar_pedido, name='cancelar_pedido'),
    # Cozinha
    path('cozinha_quente/', views.cozinha_quente, name='cozinha_quente'),
    path('cozinha_fria/', views.cozinha_fria, name='cozinha_fria'),

]
