import uuid

from mongoengine.fields import (
    BooleanField,
    StringField,
    IntField,
    FloatField,
    ReferenceField,
    DictField,
    DateTimeField,
    ListField
)
from mongoengine import Document

from app.core.helpers import local_now


class BaseDocument:
    """Document base to inherit all models

    Attributes:
        updated_at (datetime.datetime)
        created_at (datetime.datetime)
        deleted_at (datetime.datetime)
        deleted_by (DictField)
    """
    updated_at = DateTimeField(required=False)
    created_at = DateTimeField(default=local_now())
    deleted_at = DateTimeField(required=False)
    deleted_by = DictField(required=False)

    def update(self):
        self.updated_at = local_now()
        self.save()


class CustomerModel(BaseDocument, Document):
    meta = {
        "collection": "customers",
        "indexes": ["email"]
    }

    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    address = StringField()
    is_active = BooleanField(default=True)

    def to_json(self):

        return {
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "is_active": self.is_active
        }


class ProductModel(BaseDocument, Document):
    meta = {
        "collection": "product",
        "indexes": ["sku", "product_id"]
    }

    product_id = StringField(default="")
    sku = StringField(default="")
    name = StringField(default="")
    description = StringField()
    stock = IntField(default=100)
    price = FloatField(required=True)

    def to_json(self):

        return {
            "sku": self.sku,
            "name": self.name,
            "description": self.description,
            "stock": self.stock,
            "price": self.price
        }


class OrderModel(BaseDocument, Document):
    meta = {
        "collection": "order",
        "indexes": ["order_id"]
    }

    order_id = StringField(default=lambda: str(uuid.uuid4()))
    customer = ReferenceField(CustomerModel, required=True)
    products = ListField(ReferenceField(ProductModel), required=True)
    total_amount = FloatField(required=True)

    def to_json(self):

        return {
            "order_id": self.order_uuid,
            "customer": self.customer.to_json(),
            "products": [prod.to_json() for prod in self.products],
            "total_amount": self.total_amount
        }
