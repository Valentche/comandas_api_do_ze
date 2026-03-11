from pydantic import BaseModel

class Funcionario(BaseModel):
    id_funcionario: int = None
    nome: str
    matricula: str
    cpf: str
    telefone: str = None
    grupo: int
    senha: str = None

    #PABLO VALENTE NETO - 2026.1 - UNIPLAC - DESENVOLVIMENTO WEB - AULA 03-20