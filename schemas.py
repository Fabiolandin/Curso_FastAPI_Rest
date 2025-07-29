from pydantic import BaseModel
from typing import Optional, List


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

class ItemPedidoSchema(BaseModel):
    quantidade: int
    sabor: str
    tamanho: str
    preco_unitario: float

    class config:
        from_attributes = True

#Personalizando resposta do software
class ResponsePedidoSchema(BaseModel):
    id: int
    status: str
    preco: float
    itens: List[ItemPedidoSchema]
    
    class config:
        from_attributes = True