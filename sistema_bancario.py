import json

def carregar_json():
    with open("sistema.json", "r") as arquivo:
        leitura = json.load(arquivo)
    return leitura

def dump_json(novos_dados):
    with open("sistema.json", "w") as arquivo:
        json.dump(novos_dados, arquivo)

def gerar_id():
    arquivo = carregar_json()
    arquivo["last_id"] += 1
    dump_json(arquivo)
    return arquivo["last_id"]

def criar_usuario(nome):
    dados = {
        "id": gerar_id(),
        "nome": nome,
        "dinheiro": 0
    }
    arquivo = carregar_json()
    arquivo["usuarios"].append(dados)
    dump_json(arquivo)

def buscar_por_id(id):
    arquivo = carregar_json() # {"usuarios": [{"id": 1, "nome": "gabriel", "dinheiro": 0}, {"id": 2, "nome": "pedro", "dinheiro": 0}, {"id": 3, "nome": "moraes", "dinheiro": 0}], "last_id": 3}
    lista_de_usuarios = arquivo["usuarios"] # [{"id": 1, "nome": "gabriel", "dinheiro": 0}, {"id": 2, "nome": "pedro", "dinheiro": 0}, {"id": 3, "nome": "moraes", "dinheiro": 0}]
    if lista_de_usuarios == []:
        return "Sem usuarios!"
    for usuario in lista_de_usuarios:
        if usuario["id"] == id:
#             return f"""
# ID: {usuario["id"]}
# Nome: {usuario["nome"]}
# Dinheiro: {usuario["dinheiro"]}
#         """ retorno bonito porem inutilizavel
            return usuario
    return "Usuario não encontrado!"

def modificar_dinheiro(id, dinheiro):
    arquivo = carregar_json()
    usuario = buscar_por_id(id)
    if isinstance(usuario, str):
        return "Usuario não encontrado!"
    index_usuario = arquivo["usuarios"].index(usuario)
    usuario["dinheiro"] = dinheiro
    arquivo["usuarios"][index_usuario] = usuario
    # lista[0] = valor
    dump_json(arquivo)
