def test_listar_tarefas_sem_cadastros(client):
    resposta = client.get("/tarefas")

    assert resposta.status_code == 200
    assert resposta.json()["tarefas"] == []


def test_listar_todas_as_tarefas(client):
    client.post(
        "/tarefas",
        json={"titulo": "Estudar Python"}
    )
    client.post(
        "/tarefas",
        json={"titulo": "Estudar FastAPI"}
    )

    resposta = client.get("/tarefas")

    assert resposta.status_code == 200
    assert len(resposta.json()["tarefas"]) == 2


def test_tarefas_retornadas_contem_campos_esperados(client):
    client.post(
        "/tarefas",
        json={"titulo": "Estudar Pytest"}
    )

    resposta = client.get("/tarefas")
    tarefa = resposta.json()["tarefas"][0]

    campos = [
        "id",
        "titulo",
        "descricao",
        "concluida",
        "tags",
        "data_criacao",
        "data_atualizacao"
    ]

    for campo in campos:
        assert campo in tarefa


def test_quantidade_de_tarefas_retornadas(client):
    for numero in range(3):
        client.post(
            "/tarefas",
            json={"titulo": f"Tarefa {numero + 1}"}
        )

    resposta = client.get("/tarefas")

    assert resposta.json()["total"] == 3
    assert len(resposta.json()["tarefas"]) == 3
