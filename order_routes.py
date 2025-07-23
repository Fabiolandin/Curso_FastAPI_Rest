from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

#Criando a rota /pedidos/
@order_router.get("/")
async def pedidos():
    return {"Mensagem": "Você acessou a rota de pedidos"}