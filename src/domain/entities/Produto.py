from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    preco: float
    foto: bytes | None = None #Para a foto se opcional

    #PABLO VALENTE NETO - 2026.1 - UNIPLAC - DESENVOLVIMENTO WEB - AULA 03-20