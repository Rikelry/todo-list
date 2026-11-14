def test_atualizar_titulo_e_descricao(client):
    criacao = client.post(
        "/tarefas",
        json={"titulo": "Título antigo", "descricao": "Descrição antiga"}
    )

    tarefa_id = criacao.json()["id"]

    resposta = client.put(
        f"/tarefas/{tarefa_id}",
        json={
            "titulo": "Título atualizado",
            "descricao": "Descrição atualizada",
            "concluida": False,
            "tags": []
        }
    )

    assert resposta.status_code == 200
    assert resposta.json()["titulo"] == "Título atualizado"
    assert resposta.json()["descricao"] == "Descrição atualizada"


def test_alterar_tarefa_pendente_para_concluida(client):
    criacao = client.post(
        "/tarefas",
        json={"titulo": "Estudar Python"}
    )

    tarefa_id = criacao.json()["id"]

    resposta = client.put(
        f"/tarefas/{tarefa_id}",
        json={
            "titulo": "Estudar Python",
            "descricao": "",
            "concluida": True,
            "tags": []
        }
    )

    assert resposta.status_code == 200
    assert resposta.json()["concluida"] is True


def test_atualizar_tags_da_tarefa(client):
    criacao = client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Python",
            "tags": ["Python"]
        }
    )

    tarefa_id = criacao.json()["id"]

    resposta = client.put(
        f"/tarefas/{tarefa_id}",
        json={
            "titulo": "Estudar Python",
            "descricao": "",
            "concluida": False,
            "tags": ["FastAPI", "Pytest"]
        }
    )

    assert resposta.status_code == 200
    assert resposta.json()["tags"] == ["FastAPI", "Pytest"]


def test_data_atualizacao_modificada(client):
    criacao = client.post(
        "/tarefas",
        json={"titulo": "Estudar Python"}
    )

    tarefa_id = criacao.json()["id"]
    data_anterior = criacao.json()["data_atualizacao"]

    resposta = client.put(
        f"/tarefas/{tarefa_id}",
        json={
            "titulo": "Estudar Python atualizado",
            "descricao": "",
            "concluida": False,
            "tags": []
        }
    )

    assert resposta.status_code == 200
    assert resposta.json()["data_atualizacao"] != data_anterior


def test_data_criacao_permanece_inalterada(client):
    criacao = client.post(
        "/tarefas",
        json={"titulo": "Estudar Python"}
    )

    tarefa_id = criacao.json()["id"]
    data_criacao = criacao.json()["data_criacao"]

    resposta = client.put(
        f"/tarefas/{tarefa_id}",
        json={
            "titulo": "Estudar Python atualizado",
            "descricao": "",
            "concluida": False,
            "tags": []
        }
    )

    assert resposta.status_code == 200
    assert resposta.json()["data_criacao"] == data_criacao


"""
def test_atualizar_tarefa_inexistente(client):
    resposta = client.put(
        "/tarefas/999",
        json={
            "titulo": "Tarefa inexistente",
            "descricao": "",
            "concluida": False,
            "tags": []
        }
    )

    assert resposta.status_code == 404
"""


def test_atualizar_tarefa_inexistente(client):
    resposta = client.put(
        "/tarefas/999",
        json={
            "titulo": "Tarefa inexistente",
            "descricao": "",
            "concluida": False,
            "tags": []
        }
    )

    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Tarefa não encontrada"
