from fastapi import FastAPI
from settings import HOST, PORT, RELOAD
import uvicorn

#import das classes com as rotas/endpoints
from routers import FuncionarioRouter
from routers import ClienteRouter

app = FastAPI()

#mapeamento de rotas/endpoints
app.include_router(FuncionarioRouter.router)
app.include_router(ClienteRouter.router)

if __name__ == "__main__":
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=RELOAD)