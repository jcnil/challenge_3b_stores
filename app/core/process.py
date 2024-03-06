import json

from app.core.exceptions import NotFoundException
from app.core.querysets import Queryset
from app.core.constants import OK



class ProductProcess:
    @staticmethod
    def register(request) -> dict:
        
        product_id = request.get('product_id')
        prod = Queryset.get_product_by_product_id(
            product_id=product_id
        )
  
        if not prod:

            Queryset.create_product(request)

            return {
                "status": OK,
                "message": "Registered",
                "data": request
            }

        return {
            "status": OK,
            "message": "Exist Product in Local Database",
            "data": request
        }

    @staticmethod
    def get_product(
        product_id
    ) -> dict:
        """
        this function record user verification
        steps and publish in a sns
        :param request: credit_request_uid
        :return: response dictionary
        """
        prod = Queryset.get_product_by_product_id(
            product_id=product_id
        )

        if prod is not None:
            return {
                "status": OK,
                "message": "Exist Product in Local Database",
                "data": {
                    "product_id": prod.product_id,
                    "sku": prod.sku,
                    "name": prod.name,
                    "description": prod.description,
                    "stock": prod.stock,
                    "price": prod.price
                }
            }
        raise NotFoundException
    
    @staticmethod
    def update_stock(
        product_id, 
        stock
    ) -> dict:
        prod = Queryset.update_stock_product(
            product_id=product_id,
            stock=stock
        )

        if prod is not None:
            return {
                "status": OK,
                "message": "Update stock of Product in Local Database",
                "data": {
                    "product_id": prod.product_id,
                    "sku": prod.sku,
                    "name": prod.name,
                    "description": prod.description,
                    "stock": prod.stock,
                    "price": prod.price
                }
            }
        raise NotFoundException


class OrderProcess:
    @staticmethod
    def register(request) -> dict:
        
        order_id = request.get('order_id')
        order = Queryset.get_order_by_order_id(
            order_id=order_id
        )
  
        if not order:

            Queryset.create_order(request)

            return {
                "status": OK,
                "message": "Registered",
                "data": request
            }

        return {
            "status": OK,
            "message": "Exist Order in Local Database",
            "data": request
        }
