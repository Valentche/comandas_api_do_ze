from fastapi import APIRouter

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE
@router.get("/funcionario/", tags=["Funcionário"], status_code=200)
def get_funcionario():
    return {"msg": "funcionario get todos executado"}

@router.get("/funcionario/{id}", tags=["Funcionário"], status_code=200)
def get_funcionario(id: int):
    return {"msg": "funcionario get um executado"}

@router.post("/funcionario/", tags=["Funcionário"], status_code=200)
def post_funcionario():
    return {"msg": "funcionario post executado"}

@router.put("/funcionario/{id}", tags=["Funcionário"], status_code=200)
def put_funcionario(id: int):
    return {"msg": "funcionario put executado"}

@router.delete("/funcionario/{id}", tags=["Funcionário"], status_code=200)
def delete_funcionario(id: int):
    return {"msg": "funcionario delete executado", "id":id}