from app.core.process import ProductProcess, OrderProcess


class ProductHandler:
    @staticmethod
    def register_product(request):
        obj = ProductProcess()
        return obj.register(request)
    
    @staticmethod
    def get_product(product_id):
        obj = ProductProcess()
        return obj.get_product(product_id)


    @staticmethod
    def update_stock(product_id,stock):
        obj = ProductProcess()
        return obj.update_stock(product_id,stock)


class OrderHandler:
    @staticmethod
    def register_order(request):
        obj = OrderProcess()
        return obj.register(request)
