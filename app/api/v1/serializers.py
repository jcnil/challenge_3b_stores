import uuid

from typing import Optional, Union, List

from pydantic import BaseModel, Field

from app.core.models import ProductModel


class ResponseSerializer(BaseModel):
    status: Optional[str] = Field(
        title="Status Code",
    )
    data: Optional[dict] = Field(
        title="Response data",
    )
    message: Optional[str] = Field(
        title="Complementary message",
    )
    errors: Optional[Union[dict, list]] = Field(
        title="Retrieves a list of errors if an action fails",
    )


class MetaDataSerializer(BaseModel):
    text: str = Field(
        title="Text"
    )
    url: str = Field(
        title="Public url of the file"
    )


class ProductInput(BaseModel):
    product_id: str = Field(
        title="product_id",
        default=str(uuid.uuid4())
    ) 
    sku: str = Field(
        title="SKU"
    )
    name: str = Field(
        title="Name of Product",
        default=""
    )
    description: str = Field(
        title="Description of Product",
        default=""
    )
    stock: int = Field(
        title="Stock of Product by default is 100 unit",
        default=100
    )
    price: float = Field(
        title="Price of Product in mexican pesos MXN"
    )


class StockInput(BaseModel):
    stock: int = Field(
        title="Stock of Product by default is 100 unit",
        default=100
    )


class Customer(BaseModel):
    name: str = Field(
        title="Name of Customer"
    )
    email: str = Field(
        title="Email of Customer",
        unique=True
    )
    address: str = Field(
        title="Address of Customer"
    )



class OrderInput(BaseModel):
    order_id: str = Field(
        title="Order ID",
        default=str(uuid.uuid4())
    )
    customer: Customer
    products: List[ProductInput]
    total_amount: float = Field(
        title="Total Amount of Order"
    )
