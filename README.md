# To-Do List API

API REST desenvolvida em Python com FastAPI e Pydantic para gerenciamento de tarefas.

O projeto permite cadastrar, consultar, atualizar, listar e excluir tarefas, além de oferecer filtros, ordenação e paginação.

## Tecnologias utilizadas

- **Python 3.15**
- **FastAPI:** construção da API REST.
- **Pydantic:** validação e estruturação dos dados.
- **Uvicorn:** servidor de desenvolvimento utilizado pelo FastAPI CLI.
- **uv:** gerenciamento de dependências e ambiente virtual.
- **Pytest:** execução dos testes automatizados.
- **HTTPX:** suporte às requisições durante os testes.

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
.
├── pyproject.toml
├── README.md
├── src
│   └── todo_list
│       ├── main.py
│       ├── routers
│       │   └── tarefas.py
│       ├── schemas
│       │   └── tarefa.py
│       └── services
│           └── tarefa.py
├── tests
│   ├── conftest.py
│   ├── test_atualizar.py
│   ├── test_buscar.py
│   ├── test_criar.py
│   ├── test_excluir.py
│   ├── test_filtrar.py
│   ├── test_listar.py
│   ├── test_ordenar.py
│   └── test_validar.py
└── uv.lock

12 directories, 42 files
```

### Organização

- **main.py:** inicialização da aplicação FastAPI e registro das rotas.
- **routers/:** definição dos endpoints da API.
- **schemas/:** modelos e validação dos dados com Pydantic.
- **services/:** regras de negócio e operações sobre as tarefas.
- **tests/:** testes automatizados para verificar os endpoints, filtros, ordenação e validações da API.

## Instalação e execução

Clone o repositório.

```bash
git clone https://github.com/Rikelry/todo-list.git
```

Acesse a pasta do projeto.

```bash
cd todo-list
```

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

## Documentação da API

Com a aplicação em execução, a documentação interativa pode ser acessada pelos seguintes endereços:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Pela documentação, é possível visualizar os endpoints, consultar os parâmetros e realizar requisições diretamente pela interface.

## Endpoints

| Método | Endpoint               | Descrição               |
| ------ | ---------------------- | ----------------------- |
| GET    | `/`                    | Rota inicial            |
| POST   | `/tarefas`             | Cadastrar tarefa        |
| GET    | `/tarefas`             | Listar tarefas          |
| GET    | `/tarefas/{tarefa_id}` | Consultar tarefa por ID |
| PUT    | `/tarefas/{tarefa_id}` | Atualizar tarefa        |
| DELETE | `/tarefas/{tarefa_id}` | Excluir tarefa          |

## Modelo de tarefa

Cada tarefa possui os seguintes atributos:

| Campo            | Tipo        | Descrição                         |
| ---------------- | ----------- | --------------------------------- |
| id               | `int`       | Identificador único               |
| titulo           | `str`       | Título da tarefa                  |
| descricao        | `str`       | Descrição da tarefa               |
| concluida        | `bool`      | Situação da tarefa                |
| tags             | `list[str]` | Lista de etiquetas                |
| data_criacao     | `datetime`  | Data e hora de criação            |
| data_atualizacao | `datetime`  | Data e hora da última atualização |

As datas são geradas automaticamente pela aplicação.

## Filtros, ordenação e paginação

O endpoint `GET /tarefas` aceita os seguintes parâmetros:

| Parâmetro   | Descrição                                       |
| ----------- | ----------------------------------------------- |
| concluida   | Filtra tarefas por situação                     |
| tag         | Filtra tarefas por tag                          |
| titulo      | Busca por trecho do título                      |
| ordenar_por | Campo utilizado na ordenação                    |
| ordem       | Ordem crescente (`asc`) ou decrescente (`desc`) |
| pagina      | Número da página                                |
| limite      | Quantidade de tarefas por página                |
| data_inicio | Data inicial de criação                         |
| data_fim    | Data final de criação                           |

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

| Código   | Descrição                        |
| -------- | -------------------------------- |
| `200`    | Requisição realizada com sucesso |
| `201`    | Tarefa cadastrada com sucesso    |
| `204`    | Tarefa excluída com sucesso      |
| `404`    | Tarefa não encontrada            |
| `422`    | Dados ou parâmetros inválidos    |

## Testes automatizados

O projeto utiliza Pytest para verificar o funcionamento dos endpoints, as regras de negócio, os filtros, a ordenação e o tratamento de erros.

### Organização dos testes

Os testes estão separados por funcionalidade:

| Arquivo             | Cenários testados                          |
| ------------------- | ------------------------------------------ |
| `test_atualizar.py` | Atualização de tarefas e datas.            |
| `test_buscar.py`    | Consulta por identificador.                |
| `test_criar.py`     | Criação e validação de tarefas.            |
| `test_excluir.py`   | Exclusão de tarefas.                       |
| `test_filtrar.py`   | Filtros individuais e combinados.          |
| `test_listar.py`    | Listagem de tarefas.                       |
| `test_ordenar.py`   | Ordenação crescente e decrescente.         |
| `test_validar.py`   | Validação de dados e parâmetros inválidos. |

O arquivo `conftest.py` contém a fixture `client`, responsável por criar o `TestClient` e preparar o armazenamento em memória antes de cada teste.

### Executar os testes

Para executar toda a suíte:

```bash
uv run pytest -v
```

Para executar os testes de um arquivo específico:

```bash
uv run pytest tests/test_criar.py -v
```

### Resultado dos testes

A suíte automatizada conta com **46 testes aprovados**, cobrindo os principais comportamentos da aplicação.

```Bash
46 passed
0 failed
```

## Armazenamento dos dados

Os dados são armazenados em memória durante a execução da aplicação. Portanto, as tarefas não são persistidas após o encerramento ou reinicialização do servidor.

## Objetivo do projeto

Este projeto foi desenvolvido como atividade prática para consolidar conhecimentos sobre desenvolvimento de APIs REST com Python, utilizando FastAPI, Pydantic e Pytest.

O desenvolvimento contempla operações CRUD, validação de dados, filtros, ordenação, paginação, tratamento de erros e testes automatizados.
