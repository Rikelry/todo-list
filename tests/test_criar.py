def test_criar_tarefa_com_dados_validos(client):
    resposta = client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Pytest",
            "descricao": "Aprender testes automatizados",
            "tags": ["Python", "FastAPI"]
        }
    )

    assert resposta.status_code == 201


def test_criar_tarefa_contem_campos_obrigatorios(client):
    resposta = client.post(
        "/tarefas",
        json={"titulo": "Estudar Pytest"}
    )

    dados = resposta.json()

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
        assert campo in dados


def test_identificador_gerado_automaticamente(client):
    resposta = client.post(
        "/tarefas",
        json={"titulo": "Estudar Pytest"}
    )

    assert resposta.json()["id"] == 1


def test_tarefa_criada_como_nao_concluida(client):
    resposta = client.post(
        "/tarefas",
        json={"titulo": "Estudar Pytest"}
    )

    assert resposta.json()["concluida"] is False


def test_datas_preenchidas_automaticamente(client):
    resposta = client.post(
        "/tarefas",
        json={"titulo": "Estudar Pytest"}
    )

    dados = resposta.json()

    assert dados["data_criacao"] is not None
    assert dados["data_atualizacao"] is not None


def test_criar_tarefa_com_varias_tags(client):
    resposta = client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Pytest",
            "tags": ["Python", "FastAPI", "Testes"]
        }
    )

    assert resposta.status_code == 201
    assert resposta.json()["tags"] == [
        "Python",
        "FastAPI",
        "Testes"
    ]


def test_rejeitar_tarefa_sem_titulo(client):
    resposta = client.post(
        "/tarefas",
        json={"descricao": "Tarefa sem título"}
    )

    assert resposta.status_code == 422

    erro = resposta.json()["detail"][0]

    assert erro["type"] == "missing"
    assert erro["loc"] == ["body", "titulo"]
    assert erro["msg"] == "Field required"
