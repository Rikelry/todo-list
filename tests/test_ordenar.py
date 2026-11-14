def test_ordenar_por_data_criacao_crescente(client):
    client.post("/tarefas", json={"titulo": "Tarefa A"})
    client.post("/tarefas", json={"titulo": "Tarefa B"})
    client.post("/tarefas", json={"titulo": "Tarefa C"})

    resposta = client.get(
        "/tarefas?ordenar_por=data_criacao&ordem=asc"
    )

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]
    datas = [tarefa["data_criacao"] for tarefa in tarefas]

    assert datas == sorted(datas)


def test_ordenar_por_data_criacao_decrescente(client):
    client.post("/tarefas", json={"titulo": "Tarefa A"})
    client.post("/tarefas", json={"titulo": "Tarefa B"})
    client.post("/tarefas", json={"titulo": "Tarefa C"})

    resposta = client.get(
        "/tarefas?ordenar_por=data_criacao&ordem=desc"
    )

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]
    datas = [tarefa["data_criacao"] for tarefa in tarefas]

    assert datas == sorted(datas, reverse=True)


def test_ordenar_por_data_atualizacao_crescente(client):
    primeira = client.post("/tarefas", json={"titulo": "Tarefa A"})
    segunda = client.post("/tarefas", json={"titulo": "Tarefa B"})
    terceira = client.post("/tarefas", json={"titulo": "Tarefa C"})

    for criacao in [primeira, segunda, terceira]:
        tarefa_id = criacao.json()["id"]
        client.put(
            f"/tarefas/{tarefa_id}",
            json={
                "titulo": criacao.json()["titulo"],
                "descricao": "",
                "concluida": False,
                "tags": []
            }
        )

    resposta = client.get(
        "/tarefas?ordenar_por=data_atualizacao&ordem=asc"
    )

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]
    datas = [tarefa["data_atualizacao"] for tarefa in tarefas]

    assert datas == sorted(datas)


def test_ordenar_por_data_atualizacao_decrescente(client):
    primeira = client.post("/tarefas", json={"titulo": "Tarefa A"})
    segunda = client.post("/tarefas", json={"titulo": "Tarefa B"})
    terceira = client.post("/tarefas", json={"titulo": "Tarefa C"})

    for criacao in [primeira, segunda, terceira]:
        tarefa_id = criacao.json()["id"]
        client.put(
            f"/tarefas/{tarefa_id}",
            json={
                "titulo": criacao.json()["titulo"],
                "descricao": "",
                "concluida": False,
                "tags": []
            }
        )

    resposta = client.get(
        "/tarefas?ordenar_por=data_atualizacao&ordem=desc"
    )

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]
    datas = [tarefa["data_atualizacao"] for tarefa in tarefas]

    assert datas == sorted(datas, reverse=True)


def test_ordenar_por_titulo_crescente(client):
    client.post("/tarefas", json={"titulo": "Zebra"})
    client.post("/tarefas", json={"titulo": "Abacaxi"})
    client.post("/tarefas", json={"titulo": "Macaco"})

    resposta = client.get(
        "/tarefas?ordenar_por=titulo&ordem=asc"
    )

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]
    titulos = [tarefa["titulo"] for tarefa in tarefas]

    assert titulos == sorted(titulos)


def test_ordenar_por_titulo_decrescente(client):
    client.post("/tarefas", json={"titulo": "Zebra"})
    client.post("/tarefas", json={"titulo": "Abacaxi"})
    client.post("/tarefas", json={"titulo": "Macaco"})

    resposta = client.get(
        "/tarefas?ordenar_por=titulo&ordem=desc"
    )

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]
    titulos = [tarefa["titulo"] for tarefa in tarefas]

    assert titulos == sorted(titulos, reverse=True)


def test_ordenar_por_id_crescente(client):
    client.post("/tarefas", json={"titulo": "Tarefa A"})
    client.post("/tarefas", json={"titulo": "Tarefa B"})
    client.post("/tarefas", json={"titulo": "Tarefa C"})

    resposta = client.get(
        "/tarefas?ordenar_por=id&ordem=asc"
    )

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]
    ids = [tarefa["id"] for tarefa in tarefas]

    assert ids == sorted(ids)


def test_ordenar_por_id_decrescente(client):
    client.post("/tarefas", json={"titulo": "Tarefa A"})
    client.post("/tarefas", json={"titulo": "Tarefa B"})
    client.post("/tarefas", json={"titulo": "Tarefa C"})

    resposta = client.get(
        "/tarefas?ordenar_por=id&ordem=desc"
    )

    assert resposta.status_code == 200

    tarefas = resposta.json()["tarefas"]
    ids = [tarefa["id"] for tarefa in tarefas]

    assert ids == sorted(ids, reverse=True)
