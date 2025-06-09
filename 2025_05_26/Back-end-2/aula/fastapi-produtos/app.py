from fastapi import FastAPI
from models.products import Product
from models.products import CreateProduct

app = FastAPI()

data = [
    Product(id=1, nome="Produto A", preco=10.0, descricao="Produto A"),
    Product(id=2, nome="Produto B", preco=20.0, descricao="Produto B"),
    Product(id=3, nome="Produto C", preco=30.0, descricao="Produto C"),
]

@app.get("/api/products")
def get_products():
    """
    Método para exibir todos os produtos.
    """
    return data

@app.get("/api/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in data:
        if product.id == product_id:
            return product
    return {"Message": "Produto não encontrado"}, 404

@app.post("/api/products")
def create_product(product: CreateProduct):
    new_product = Product(id=len(data) + 1, **product.dict())
    data.append(new_product)
    return product

@app.delete("/api/products/{product_id}")
def delete_product(product_id: int):
    for i, product in enumerate(data):
        if product.id == product_id:
            deleted = data.pop(i)
            return {
                "Message": "Produto deletado com sucesso",
                "Produto": deleted
            }        
    return {"Message": "ID não encontrado"}, 404

@app.put("/api/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for i, product in enumerate(data):
        if product.id == product_id:            
            data[i] = updated_product
            return {
                "Message": "Produto atualizado com sucesso",
                "Produto": updated_product
            }
    return {"Message": "ID não encontrado"}, 404