from fastapi import FastAPI

from todo_list.routers.tarefas import router as tarefas_router


app = FastAPI(
    title="To-Do List API",
    description="API para gerenciamento de tarefas",
    version="1.0.0",
)


# REGISTRO DAS ROTAS
app.include_router(tarefas_router)


# ROTA PRINCIPAL
@app.get("/")
def root():
    return {"message": "Bem-vindo à To-Do List API!"}
