from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_inicial, name='tela_inicial'),
    path('jogar/', views.menu_jogo, name='menu_jogo'),
    path('jogar/<int:personagem_id>/', views.jogar, name='jogar'),
    path('personagens/', views.listar_personagens, name='listar_personagens'),
    path('criar_personagem/', views.criar_personagem, name='criar_personagem'),
    path('editar_personagem/<int:personagem_id>/', views.editar_personagem, name='editar_personagem'),
     # População de dados da API
    path('popular_dados/', views.popular_dados_api, name='popular_dados'),
    path('deletar_personagem/<int:personagem_id>/', views.deletar_personagem, name='deletar_personagem')
]