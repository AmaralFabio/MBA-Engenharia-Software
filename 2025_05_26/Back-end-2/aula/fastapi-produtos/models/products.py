from pydantic import BaseModel;

class Product(BaseModel):
    """
    Modelo de dados para um produto.
    Atributos:
    - id: int - Identificador único do produto.
    - nome: str - Nome do produto.
    - preco: float - Preço do produto.
    - descricao: str - Descrição do produto.
    """
    id: int
    nome: str
    preco: float
    descricao: str

class CreateProduct(BaseModel): 
    """
    Modelo de dados para criar um novo produto.
    Atributos:
    - nome: str - Nome do produto.
    - preco: float - Preço do produto.
    - descricao: str - Descrição do produto.
    """
    nome: str
    preco: float
    descricao: str