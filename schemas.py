from pydantic import BaseModel
from typing import Optional


class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_attributes = True

class PedidoSchema(BaseModel):
    usuario: int

    class config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class config:
        from_attributes = True