def test_buscar_tarefa_existente(client):
    criacao = client.post(
        "/tarefas",
        json={
            "titulo": "Estudar FastAPI",
            "descricao": "Revisar os endpoints",
            "tags": ["Python", "FastAPI"]
        }
    )

    tarefa_id = criacao.json()["id"]

    resposta = client.get(f"/tarefas/{tarefa_id}")

    assert resposta.status_code == 200


def test_buscar_tarefa_com_dados_corretos(client):
    dados = {
        "titulo": "Estudar Pytest",
        "descricao": "Aprender testes automatizados",
        "tags": ["Python", "Testes"]
    }

    criacao = client.post("/tarefas", json=dados)
    tarefa_id = criacao.json()["id"]

    resposta = client.get(f"/tarefas/{tarefa_id}")
    tarefa = resposta.json()

    assert tarefa["id"] == tarefa_id
    assert tarefa["titulo"] == dados["titulo"]
    assert tarefa["descricao"] == dados["descricao"]
    assert tarefa["concluida"] is False
    assert tarefa["tags"] == dados["tags"]



def test_buscar_tarefa_inexistente(client):
    resposta = client.get("/tarefas/999")

    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Tarefa não encontrada"
