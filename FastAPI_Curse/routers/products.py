from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"], responses={404: {"description": "No encontrado"}})

products_list = ["product1", "product2", "product3,", "product4", "product5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]