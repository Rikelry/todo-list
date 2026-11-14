def test_rejeitar_valor_textual_no_campo_concluida(client):
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
            "concluida": "texto inválido",
            "tags": []
        }
    )

    assert resposta.status_code == 422

    detalhes = resposta.json()["detail"]
    assert detalhes

    assert any(
        "concluida" in str(erro["loc"])
        for erro in detalhes
    )


def test_rejeitar_parametro_ordenar_por_invalido(client):
    resposta = client.get(
        "/tarefas?ordenar_por=preco"
    )

    assert resposta.status_code == 422

    detalhes = resposta.json()["detail"]
    assert any(
        "ordenar_por" in str(erro["loc"])
        for erro in detalhes
    )


def test_rejeitar_parametro_ordem_invalido(client):
    resposta = client.get(
        "/tarefas?ordem=crescente"
    )

    assert resposta.status_code == 422

    detalhes = resposta.json()["detail"]
    assert any(
        "ordem" in str(erro["loc"])
        for erro in detalhes
    )
