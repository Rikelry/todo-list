import pytest
from fastapi.testclient import TestClient

from todo_list.main import app
from todo_list.services import tarefa as tarefa_service


@pytest.fixture
def client():
    # LIMPA O ARMAZENAMENTO ANTES DE CADA TESTE
    tarefa_service.tarefas.clear()
    tarefa_service.proximo_id = 1

    # CRIA O CLIENTE DE TESTES
    with TestClient(app) as test_client:
        yield test_client
