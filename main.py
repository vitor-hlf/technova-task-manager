from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="TechNova Task Manager API")

class Task(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluida: bool = False

db_tarefas: List[Task] = []
id_controlador = 1

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à TechNova Task Manager API!"}

@app.post("/tarefas", response_model=Task, status_code=201)
def criar_tarefa(task: Task):
    global id_controlador
    task.id = id_controlador
    db_tarefas.append(task)
    id_controlador += 1
    return task

@app.get("/tarefas", response_model=List[Task])
def listar_tarefas():
    return db_tarefas

@app.put("/tarefas/{tarefa_id}", response_model=Task)
def atualizar_tarefa(tarefa_id: int, task_atualizada: Task):
    for index, task in enumerate(db_tarefas):
        if task.id == tarefa_id:
            task_atualizada.id = tarefa_id
            db_tarefas[index] = task_atualizada
            return task_atualizada
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    for index, task in enumerate(db_tarefas):
        if task.id == tarefa_id:
            db_tarefas.pop(index)
            return {"mensagem": f"Tarefa com ID {tarefa_id} excluída com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada para exclusão")