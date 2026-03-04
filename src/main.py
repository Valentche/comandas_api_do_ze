from fastapi import FastAPI
from settings import HOST, PORT, RELOAD
import uvicorn

#import das classes com as rotas/endpoints
from routers import FuncionarioRouter
from routers import ClienteRouter

# rota padrão
app = FastAPI()

@app.get("/", tags=["Root"], status_code=200)
def root():
    return {"detail":"API Pastelaria", "Swagger UI": "http://127.0.0.1:8000/docs", "ReDoc": "http://127.0.0.1:8000/redoc" }

#mapeamento de rotas/endpoints
app.include_router(FuncionarioRouter.router)
app.include_router(ClienteRouter.router)

if __name__ == "__main__":
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=RELOAD)