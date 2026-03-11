from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str

    #PABLO VALENTE NETO - 2026.1 - UNIPLAC - DESENVOLVIMENTO WEB - AULA 03-20