from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """ 
    Essa é a rota padrão de autenticação do sistema
    """
    return {"mensagem" : "Você acessou uma rota padrão de autenticação", "autenticado": False}