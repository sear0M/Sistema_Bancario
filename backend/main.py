import json
import funcoes

from fastapi import FastAPI , HTTPException

app=FastAPI()

#@app.post
@app.get("/")
def root():
    return "Raiz"

@app.get("/usuarios")
def listar_usuarios():
    return funcoes.carregar_json()["usuarios"]

@app.get("/usuarios/id/{id}")
def usuarios_id(id: int):
    return funcoes.buscar_por_id(id)

@app.get("/usuarios/nome/{nome}")
def usuarios_nomes(nome: str):
    return funcoes.buscar_nome(nome)

@app.get("/usuarios/dinheiro/{dinheiro}")
def usuarios_dinheiro(dinheiro: float):
    return funcoes.buscar_por_saldo(dinheiro)