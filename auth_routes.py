from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """ 
    Essa é a rota padrão de autenticação do sistema
    """
    return {"mensagem" : "Você acessou uma rota padrão de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):
        usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
        if usuario:
            # Já existe um usuario com este email
            return HTTPException(status_code=400, detail="E-mail do usuário já cadastrado")
        else:
            senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
            # Criar novo usuário
            novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
            session.add(novo_usuario)
            session.commit()
            return {f"mensagem": "Usuário cadastrado com sucesso! {usuario_schema.email}"}

