from datetime import datetime, date

from todo_list.schemas.tarefa import Tarefa, TarefaListResponse, TarefaCreate, TarefaUpdate


# ARMAZENAMENTO EM MEMÓRIA
tarefas: list[Tarefa] = []
proximo_id = 1


"""
Descrição do módulo.

:author: Rikelry
:version: 1.0
"""


# OPERAÇÕES
def listar_tarefas(
    concluida: bool | None = None,
    tag: str | None = None,
    titulo: str | None = None,
    ordenar_por: str = "id",
    ordem: str = "asc",
    pagina: int = 1,
    limite: int = 10,
    data_inicio: date | None = None,
    data_fim: date | None = None
) -> TarefaListResponse:

    resultado = tarefas.copy()

    # FILTRO POR SITUAÇÃO
    if concluida is not None:
        resultado = [
            tarefa for tarefa in resultado
            if tarefa.concluida == concluida
        ]

    # FILTRO POR TAG
    if tag is not None:
        resultado = [
            tarefa for tarefa in resultado
            if any(tag.casefold() == item.casefold() for item in tarefa.tags)
        ]

    # FILTRO POR TÍTULO
    if titulo is not None:
        resultado = [
            tarefa for tarefa in resultado
            if titulo.casefold() in tarefa.titulo.casefold()
        ]

    # FILTRO POR PERÍODO
    if data_inicio is not None:
        resultado = [
            tarefa for tarefa in resultado
            if tarefa.data_criacao.date() >= data_inicio
        ]

    if data_fim is not None:
        resultado = [
            tarefa for tarefa in resultado
            if tarefa.data_criacao.date() <= data_fim
        ]

    # ORDENAÇÃO
    resultado.sort(
        key=lambda tarefa: getattr(tarefa, ordenar_por),
        reverse=(ordem == "desc")
    )

    # PAGINAÇÃO
    total = len(resultado)

    inicio = (pagina - 1) * limite
    fim = inicio + limite

    tarefas_paginadas = resultado[inicio:fim]

    return TarefaListResponse(
        pagina=pagina,
        limite=limite,
        total=total,
        tarefas=tarefas_paginadas
    )


def buscar_tarefa(tarefa_id: int) -> Tarefa | None:
    for tarefa in tarefas:
        if tarefa.id == tarefa_id:
            return tarefa

    return None


def criar_tarefa(dados: TarefaCreate) -> Tarefa:
    global proximo_id

    agora = datetime.now()

    nova_tarefa = Tarefa(
        id=proximo_id,
        titulo=dados.titulo,
        descricao=dados.descricao,
        concluida=False,
        tags=dados.tags,
        data_criacao=agora,
        data_atualizacao=agora
    )

    tarefas.append(nova_tarefa)
    proximo_id += 1

    return nova_tarefa


def atualizar_tarefa(
    tarefa_id: int,
    dados: TarefaUpdate
) -> Tarefa | None:
    for indice, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            tarefa_atualizada = Tarefa(
                id=tarefa.id,
                titulo=dados.titulo,
                descricao=dados.descricao,
                concluida=dados.concluida,
                tags=dados.tags,
                data_criacao=tarefa.data_criacao,
                data_atualizacao=datetime.now()
            )

            tarefas[indice] = tarefa_atualizada
            return tarefa_atualizada

    return None


def excluir_tarefa(tarefa_id: int) -> bool:
    for indice, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            tarefas.pop(indice)
            return True

    return False
