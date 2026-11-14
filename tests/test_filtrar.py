def test_combinar_filtros_concluida_e_tag(client):
    client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Python",
            "concluida": False,
            "tags": ["python"]
        }
    )

    tarefa_concluida = client.post(
        "/tarefas",
        json={
            "titulo": "Estudar FastAPI",
            "tags": ["python"]
        }
    )

    tarefa_id = tarefa_concluida.json()["id"]

    client.put(
        f"/tarefas/{tarefa_id}",
        json={
            "titulo": "Estudar FastAPI",
            "descricao": "",
            "concluida": True,
            "tags": ["python"]
        }
    )
    client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Java",
            "concluida": False,
            "tags": ["java"]
        }
    )

    resposta = client.get("/tarefas?concluida=false&tag=python")

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]

    assert len(tarefas) == 1
    for tarefa in tarefas:
        assert tarefa["concluida"] is False
        assert "python" in tarefa["tags"]


def test_combinar_filtros_com_ordenacao(client):
    primeira = client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Python básico",
            "tags": ["python"]
        }
    )

    segunda = client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Python avançado",
            "tags": ["python"]
        }
    )

    client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Java",
            "tags": ["java"]
        }
    )

    resposta = client.get(
        "/tarefas?concluida=false&tag=python"
        "&ordenar_por=data_criacao&ordem=desc"
    )

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]

    assert len(tarefas) == 2

    for tarefa in tarefas:
        assert tarefa["concluida"] is False
        assert "python" in tarefa["tags"]

    datas = [tarefa["data_criacao"] for tarefa in tarefas]
    assert datas == sorted(datas, reverse=True)


def test_filtrar_tarefas_concluidas(client):
    client.post(
        "/tarefas",
        json={"titulo": "Tarefa pendente"}
    )

    criacao = client.post(
        "/tarefas",
        json={"titulo": "Tarefa concluída"}
    )

    tarefa_id = criacao.json()["id"]

    client.put(
        f"/tarefas/{tarefa_id}",
        json={
            "titulo": "Tarefa concluída",
            "descricao": "",
            "concluida": True,
            "tags": []
        }
    )

    resposta = client.get("/tarefas?concluida=true")

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Tarefa concluída"
    assert tarefas[0]["concluida"] is True


def test_filtrar_tarefas_concluidas_sem_resultados(client):
    client.post(
        "/tarefas",
        json={"titulo": "Tarefa pendente"}
    )

    resposta = client.get("/tarefas?concluida=true")

    assert resposta.status_code == 200
    assert resposta.json()["tarefas"] == []


def test_filtrar_tarefas_pendentes(client):
    client.post(
        "/tarefas",
        json={"titulo": "Tarefa pendente"}
    )

    criacao = client.post(
        "/tarefas",
        json={"titulo": "Tarefa concluída"}
    )

    tarefa_id = criacao.json()["id"]

    client.put(
        f"/tarefas/{tarefa_id}",
        json={
            "titulo": "Tarefa concluída",
            "descricao": "",
            "concluida": True,
            "tags": []
        }
    )

    resposta = client.get("/tarefas?concluida=false")

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Tarefa pendente"
    assert tarefas[0]["concluida"] is False


def test_filtrar_tarefas_pendentes_sem_resultados(client):
    criacao = client.post(
        "/tarefas",
        json={"titulo": "Tarefa concluída"}
    )

    tarefa_id = criacao.json()["id"]

    client.put(
        f"/tarefas/{tarefa_id}",
        json={
            "titulo": "Tarefa concluída",
            "descricao": "",
            "concluida": True,
            "tags": []
        }
    )

    resposta = client.get("/tarefas?concluida=false")

    assert resposta.status_code == 200
    assert resposta.json()["tarefas"] == []


def test_filtrar_tarefas_por_tag(client):
    client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Python",
            "tags": ["python", "estudos"]
        }
    )

    client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Java",
            "tags": ["java"]
        }
    )

    resposta = client.get("/tarefas?tag=python")

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar Python"
    assert "python" in tarefas[0]["tags"]


def test_filtrar_tarefas_por_tag_sem_resultados(client):
    client.post(
        "/tarefas",
        json={
            "titulo": "Estudar Python",
            "tags": ["python"]
        }
    )

    resposta = client.get("/tarefas?tag=java")

    assert resposta.status_code == 200
    assert resposta.json()["tarefas"] == []


def test_filtrar_tarefas_por_titulo(client):
    client.post(
        "/tarefas",
        json={"titulo": "Estudar Python"}
    )

    client.post(
        "/tarefas",
        json={"titulo": "Estudar Java"}
    )

    resposta = client.get("/tarefas?titulo=python")

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar Python"


def test_filtrar_tarefas_por_titulo_sem_resultados(client):
    client.post(
        "/tarefas",
        json={"titulo": "Estudar Python"}
    )

    resposta = client.get("/tarefas?titulo=java")

    assert resposta.status_code == 200
    assert resposta.json()["tarefas"] == []
