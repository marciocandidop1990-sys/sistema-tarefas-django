from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('nova/', views.criar_tarefa, name='criar_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),
]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/tarefas', views.TarefaViewSet)

urlpatterns += router.urls