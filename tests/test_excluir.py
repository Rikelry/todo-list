def test_excluir_tarefa_existente(client):
    criacao = client.post(
        "/tarefas",
        json={"titulo": "Tarefa para excluir"}
    )

    tarefa_id = criacao.json()["id"]

    resposta = client.delete(f"/tarefas/{tarefa_id}")

    assert resposta.status_code == 204


def test_excluir_retorna_sem_conteudo(client):
    criacao = client.post(
        "/tarefas",
        json={"titulo": "Tarefa para excluir"}
    )

    tarefa_id = criacao.json()["id"]

    resposta = client.delete(f"/tarefas/{tarefa_id}")

    assert resposta.status_code == 204
    assert resposta.content == b""


def test_tarefa_excluida_nao_aparece_na_listagem(client):
    criacao = client.post(
        "/tarefas",
        json={"titulo": "Tarefa para excluir"}
    )

    tarefa_id = criacao.json()["id"]

    client.delete(f"/tarefas/{tarefa_id}")

    resposta = client.get("/tarefas")
    ids = [tarefa["id"] for tarefa in resposta.json()["tarefas"]]

    assert tarefa_id not in ids


def test_consultar_tarefa_excluida_retorna_404(client):
    criacao = client.post(
        "/tarefas",
        json={"titulo": "Tarefa para excluir"}
    )

    tarefa_id = criacao.json()["id"]

    client.delete(f"/tarefas/{tarefa_id}")

    resposta = client.get(f"/tarefas/{tarefa_id}")

    assert resposta.status_code == 404



def test_excluir_tarefa_inexistente(client):
    resposta = client.delete("/tarefas/999")

    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Tarefa não encontrada"
