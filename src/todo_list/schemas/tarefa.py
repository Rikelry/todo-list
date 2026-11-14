from datetime import datetime

from pydantic import BaseModel, Field


class TarefaCreate(BaseModel):
    titulo: str = Field(min_length=1, max_length=100)
    descricao: str = Field(default="", max_length=500)
    tags: list[str] = Field(default_factory=list)


class TarefaUpdate(BaseModel):
    titulo: str = Field(min_length=1, max_length=100)
    descricao: str = Field(default="", max_length=500)
    concluida: bool
    tags: list[str] = Field(default_factory=list)


class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluida: bool = False
    tags: list[str] = Field(default_factory=list)
    data_criacao: datetime
    data_atualizacao: datetime


class TarefaListResponse(BaseModel):
    pagina: int
    limite: int
    total: int
    tarefas: list[Tarefa]
