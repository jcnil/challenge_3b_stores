import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.core.exceptions import ExistException, NotFoundException
from app.core.handlers import ProductHandler,OrderHandler
from app.api.v1.serializers import(
  ProductInput,
  StockInput,
  OrderInput,
  ResponseSerializer  
)
from app.core.workers import stock_alert

router = APIRouter()


@router.get(
    "/products/{product_id}",
    tags=["Products"],
    response_model=ResponseSerializer
)
async def get_product(
    product_id: str
):
    """Get product by specific product_id"""
    try:
        result = ProductHandler.get_product(
            product_id=product_id
        )
        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": str(result["message"])
            }
        )
    except NotFoundException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": product_id,
                "message": str(e.message("Document")),
                "errors": str(e)
            },
            status_code=e.status
        )


@router.post(
    "/products",
    tags=["Products"],
    response_model=ResponseSerializer
)
async def post_create_product(product: ProductInput) -> dict:
    """Post Product """
    try:
        request = product.dict()
        result = ProductHandler.register_product(request)
        stock_alert.delay(request.get('product_id'), request.get('stock'))

        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": result["message"]
            }
        )
    except ExistException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": result["data"],
                "message": str(e.message("Product")),
                "errors": str(e)
            },
            status_code=e.status
        )


@router.patch(
    "/inventories/product/{product_id}",
    tags=["Products"],
    response_model=ResponseSerializer
)
async def patch_update_product(
    product_id,
    stock: StockInput
) -> dict:
    try:
        result = ProductHandler.update_stock(product_id,stock.stock)
        stock_alert.delay(product_id, stock.stock)

        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": result["message"]
            }
        )
    except ExistException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": result["data"],
                "message": str(e.message("Product")),
                "errors": str(e)
            },
            status_code=e.status
        )


@router.post(
    "/orders ",
    tags=["Orders"],
    response_model=ResponseSerializer
)
async def post_create_order(
    order: OrderInput
) -> dict:
    """Post text to decrypted """
    try:

        result = OrderHandler.register_order(
            order.dict()
        )

        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": str(result["message"])
            }
        )
    except ExistException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": result["data"],
                "message": str(e.message("Text")),
                "errors": str(e)
            },
            status_code=e.status
        )
