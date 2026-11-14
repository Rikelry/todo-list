from datetime import date
from typing import Literal

from fastapi import APIRouter, HTTPException, Query, Path, Response, status

from todo_list.schemas.tarefa import (
    Tarefa,
    TarefaCreate,
    TarefaUpdate,
    TarefaListResponse
)
from todo_list.services import tarefa as tarefa_service


router = APIRouter(
    prefix="/tarefas",
    tags=["tarefas"]
)


# READ: listar tarefas com filtros, ordenação e paginação
@router.get("", response_model=TarefaListResponse)
def listar_tarefas(
    concluida: bool | None = None,
    tag: str | None = None,
    titulo: str | None = None,
    ordenar_por: Literal[
        "id",
        "titulo",
        "data_criacao",
        "data_atualizacao"
    ] = Query(default="id"),
    ordem: Literal["asc", "desc"] = Query(default="asc"),
    pagina: int = Query(default=1, ge=1),
    limite: int = Query(default=10, ge=1, le=100),
    data_inicio: date | None = None,
    data_fim: date | None = None
):
    if (
        data_inicio is not None
        and data_fim is not None
        and data_inicio > data_fim
    ):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="data_inicio não pode ser posterior a data_fim"
        )
        
    return tarefa_service.listar_tarefas(
        concluida=concluida,
        tag=tag,
        titulo=titulo,
        ordenar_por=ordenar_por,
        ordem=ordem,
        pagina=pagina,
        limite=limite,
        data_inicio=data_inicio,
        data_fim=data_fim
    )


# READ: consultar tarefa
@router.get("/{tarefa_id}", response_model=Tarefa)
def buscar_tarefa(tarefa_id: int = Path(gt=0)):
    tarefa = tarefa_service.buscar_tarefa(tarefa_id)

    if tarefa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )

    return tarefa


# CREATE: cadastrar tarefa
@router.post(
    "",
    response_model=Tarefa,
    status_code=status.HTTP_201_CREATED
)
def criar_tarefa(dados: TarefaCreate):
    return tarefa_service.criar_tarefa(dados)


# UPDATE: atualizar tarefa
@router.put("/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(
    dados: TarefaUpdate,
    tarefa_id: int = Path(gt=0)
):
    tarefa = tarefa_service.atualizar_tarefa(tarefa_id, dados)

    if tarefa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )

    return tarefa


# DELETE: excluir tarefa
@router.delete(
    "/{tarefa_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def excluir_tarefa(tarefa_id: int = Path(gt=0)):
    excluida = tarefa_service.excluir_tarefa(tarefa_id)

    if not excluida:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
