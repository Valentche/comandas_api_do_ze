from fastapi import APIRouter

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE
@router.get("/cliente/", tags=["Cliente"], status_code=200)
def get_cliente():
    return {"msg": "cliente get todos executado"}

@router.get("/cliente/{id}", tags=["Cliente"], status_code=200)
def get_cliente(id: int):
    return {"msg": "cliente get um executado"}

@router.post("/cliente/", tags=["Cliente"], status_code=200)
def post_cliente():
    return {"msg": "cliente post executado"}

@router.put("/cliente/{id}", tags=["Cliente"], status_code=200)
def put_cliente(id: int):
    return {"msg": "cliente put executado"}

@router.delete("/cliente/{id}", tags=["Cliente"], status_code=200)
def delete_cliente(id: int):
    return {"msg": "cliente delete executado", "id":id}