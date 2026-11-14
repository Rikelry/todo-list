# To-Do List API

API REST desenvolvida em Python com FastAPI e Pydantic para gerenciamento de tarefas.

O projeto permite cadastrar, consultar, atualizar, listar e excluir tarefas, além de oferecer filtros, ordenação e paginação.

## Tecnologias utilizadas

- **Python:** linguagem de programação.
- **FastAPI:** framework para construção da API REST.
- **Pydantic:** validação e estruturação dos dados.
- **uv:** gerenciamento de dependências e ambiente Python.

## Funcionalidades

- Cadastro de tarefas.
- Listagem de todas as tarefas.
- Consulta de tarefa por ID.
- Atualização de tarefas.
- Exclusão de tarefas.
- Controle de conclusão das tarefas.
- Cadastro de tags.
- Filtro por situação (concluída ou não concluída).
- Filtro por tag.
- Busca por parte do título, sem diferenciar maiúsculas e minúsculas.
- Ordenação crescente e decrescente.
- Paginação dos resultados.
- Consulta de tarefas por período de criação.
- Registro automático das datas de criação e atualização.
- Tratamento de erros para tarefas inexistentes e períodos inválidos.

## Estrutura do projeto

```text
todo-list/
├── src/
│   └── todo_list/
│       ├── __init__.py
│       ├── main.py
│       ├── routers/
│       │   ├── __init__.py
│       │   └── tarefas.py
│       ├── schemas/
│       │   ├── __init__.py
│       │   └── tarefa.py
│       └── services/
│           ├── __init__.py
│           └── tarefa.py
├── pyproject.toml
├── uv.lock
└── README.md
```

### Organização

- **main.py:** inicialização da aplicação FastAPI e registro das rotas.
- **routers/:** definição dos endpoints da API.
- **schemas/:** modelos e validação dos dados com Pydantic.
- **services/:** regras de negócio e operações sobre as tarefas.

## Instalação e execução

Clone o repositório e acesse a pasta do projeto.

Instale as dependências:

```bash
uv sync
```

Inicie o servidor de desenvolvimento:

```bash
uv run fastapi dev src/todo_list/main.py
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

## Documentação interativa

O FastAPI disponibiliza documentação interativa para consultar e testar os endpoints.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Rota inicial |
| POST | `/tarefas` | Cadastrar tarefa |
| GET | `/tarefas` | Listar tarefas |
| GET | `/tarefas/{tarefa_id}` | Consultar tarefa por ID |
| PUT | `/tarefas/{tarefa_id}` | Atualizar tarefa |
| DELETE | `/tarefas/{tarefa_id}` | Excluir tarefa |

## Modelo de tarefa

Cada tarefa possui os seguintes atributos:

| Campo | Tipo | Descrição |
|---|---|---|
| id | int | Identificador único |
| titulo | str | Título da tarefa |
| descricao | str | Descrição da tarefa |
| concluida | bool | Situação da tarefa |
| tags | list[str] | Lista de etiquetas |
| data_criacao | datetime | Data e hora de criação |
| data_atualizacao | datetime | Data e hora da última atualização |

As datas são geradas automaticamente pela aplicação.

## Filtros, ordenação e paginação

O endpoint `GET /tarefas` aceita os seguintes parâmetros:

| Parâmetro | Descrição |
|---|---|
| concluida | Filtra tarefas por situação |
| tag | Filtra tarefas por tag |
| titulo | Busca por trecho do título |
| ordenar_por | Campo utilizado na ordenação |
| ordem | Ordem crescente (`asc`) ou decrescente (`desc`) |
| pagina | Número da página |
| limite | Quantidade de tarefas por página |
| data_inicio | Data inicial de criação |
| data_fim | Data final de criação |

Os campos disponíveis para ordenação são:

- `id`
- `titulo`
- `data_criacao`
- `data_atualizacao`

Os filtros podem ser combinados na mesma requisição.

### Exemplo de consulta

```text
GET /tarefas?concluida=false&tag=python&ordenar_por=titulo&ordem=asc&pagina=1&limite=10
```

### Formato da resposta paginada

```json
{
  "pagina": 1,
  "limite": 10,
  "total": 2,
  "tarefas": []
}
```

## Tratamento de erros

A API utiliza códigos HTTP para indicar o resultado das operações.

| Código | Descrição |
|---|---|
| 200 | Requisição realizada com sucesso |
| 201 | Tarefa cadastrada com sucesso |
| 204 | Tarefa excluída com sucesso |
| 404 | Tarefa não encontrada |
| 422 | Dados ou parâmetros inválidos |

## Armazenamento dos dados

Nesta versão, as tarefas são armazenadas em memória, utilizando uma lista Python.

Isso significa que os dados são mantidos somente enquanto a aplicação está em execução. Ao reiniciar o servidor, as tarefas cadastradas são perdidas.

## Objetivo acadêmico

Projeto desenvolvido como atividade acadêmica para praticar o desenvolvimento de APIs REST utilizando Python, FastAPI e Pydantic, aplicando organização em camadas, validação de dados, operações CRUD, filtros, ordenação e paginação.
