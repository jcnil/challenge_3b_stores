import json

from .models import (
    ProductModel,
    OrderModel
)


class Queryset:

    @staticmethod
    def get_product_by_product_id(
        product_id
    ) -> ProductModel:
        """
        Return a product based in product_id.
        :param product_id: str
        :return: ProductModel
        """
        return ProductModel.objects(
            product_id=product_id
        ).first()

    @staticmethod
    def create_product(request) -> ProductModel:
        """
        Create an product
        :param request
        :return: ProductModel
        """
        prod = ProductModel(**request)
        prod.save()
        return prod

    @staticmethod
    def update_stock_product(product_id, stock) -> ProductModel:
        """
        Update the stock of a product.
        :param request: Dictionary containing 'product_id' and 'stock'.
        :return: ProductModel
        """
              
        product = ProductModel.objects.get(product_id=product_id)
       
        product.stock = stock
        product.save()

        return product

    @staticmethod
    def get_order_by_order_id(
        order_id
    ) -> OrderModel:
        """
        Return a order based in order_id.
        :param order_id: str
        :return: OrderModel
        """
        return OrderModel.objects(
            order_id=order_id
        ).first()
    
    @staticmethod
    def create_order(request) -> OrderModel:
        """
        Create an order
        :param request
        :return: OrderModel
        """
        order = OrderModel(**request)
        order.save()
        return order
