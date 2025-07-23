from fastapi import FastAPI

app = FastAPI()

#Importando os roteadores de rotas
from auth_routes import auth_router
from order_routes import order_router

#configurando os roteadores de rota
app.include_router(auth_router)
app.include_router(order_router)



#para executar nosso código, executar essa linha no terminal
#uvicorn main:app --reload