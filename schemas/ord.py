from typing import Optional, Any, Dict, List, Literal
from pydantic import BaseModel
from datetime import datetime
from schemas.inv import ProductAloneModel
from schemas.user import AddressModel, UserSimpleDetailsModel, MerchantModel
from schemas.misc import CurrencyModel

class OrderedProductModel(BaseModel):
    product_id: int
    quantity: int
    amount: float
    
    class Config:
        orm_mode = True

class CartProductModel(BaseModel):
    product_id: int
    quantity: int
    amount: float

    class Config:
        orm_mode = True

class CreateOrderRequest(BaseModel):
    merchant_id: Optional[int] = 0
    address_id: Optional[int] = 0
    is_account: Optional[bool] = False
    is_card: Optional[bool] = False
    card_id: Optional[int] = 0
    cart_id: Optional[int] = 0
    card_transaction_reference: Optional[str] = None
    save_card: Optional[bool] = False
    provider_code: Optional[Literal['paystack', 'flutterwave']] = None
    products: List[OrderedProductModel] = None
    amount: float
    total_amount: float
    discount: Optional[float] = 0.0
    
    class Config:
        orm_mode = True

class UpdateOrderRequest(BaseModel):
    payment_status: Optional[int] = None
    delivery_status: Optional[int] = None
    status: Optional[int] = None
    
    class Config:
        orm_mode = True

class OrderProductsModel(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    amount: float
    status: Optional[int] = 0
    created_at: Optional[datetime] = None
    product: Optional[ProductAloneModel] = None

    class Config:
        orm_mode = True


class OrderMainModel(BaseModel):
    id: int
    merchant_id: Optional[int] = 0
    reference: Optional[str] = None
    sub_total: float
    total_amount: float
    discount: Optional[float] = 0.0
    address_id: Optional[int] = 0
    status: Optional[int] = 0
    order_products: List[OrderProductsModel] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class OrderLog(BaseModel):
    id: int
    order_id: Optional[int] = None
    event_type: Optional[int] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class OrderModel(BaseModel):
    id: int
    user_id: Optional[int] = 0
    merchant_id: Optional[int] = 0
    currency_id: Optional[int] = 0
    address_id: Optional[int] = 0
    reference: Optional[str] = None
    sub_total: float
    total_amount: float
    vat: Optional[float] = 0.0
    wht: Optional[float] = 0.0
    discount: Optional[float] = 0.0
    estimated_delivery_time: Optional[str] = None
    payment_type: Optional[int] = 0
    order_detail: Optional[str] = None
    pick_up_pin: Optional[str] = None
    delivery_pin: Optional[str] = None
    is_gift: Optional[int] = 0
    receiver_phone_number: Optional[str] = None
    receiver_house_number: Optional[str] = None
    receiver_street: Optional[str] = None
    receiver_nearest_bus_stop: Optional[str] = None
    receiver_city: Optional[str] = None
    receiver_state: Optional[str] = None
    receiver_country: Optional[str] = None
    receiver_latitude: Optional[str] = None
    receiver_longitude: Optional[str] = None
    rejection_reason: Optional[str] = None
    cancellation_reason: Optional[str] = None
    payment_status: Optional[int] = 0
    delivery_status: Optional[int] = 0
    status: Optional[int] = 0
    created_at: Optional[datetime] = None
    order_products: List[OrderProductsModel] = None
    user: Optional[UserSimpleDetailsModel] = None
    address: Optional[AddressModel] = None
    currency: Optional[CurrencyModel] = None
    order_logs: Optional[List[OrderLog]] = None

    class Config:
        orm_mode = True

class NewOrderResponse(BaseModel):
    status: bool
    message: str
    data: Optional[OrderModel] = None

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    status: bool
    message: str
    data: Optional[OrderModel] = None

    class Config:
        orm_mode = True

class CartProductModel(BaseModel):
    id: int
    cart_id: int
    product_id: int
    quantity: int
    amount: float
    status: Optional[int] = 0
    created_at: Optional[datetime] = None
    product: Optional[ProductAloneModel] = None

    class Config:
        orm_mode = True

class CartModel(BaseModel):
    id: int
    user_id: int
    reference: str
    total_amount: Optional[float] = 0
    status: Optional[int] = 0
    created_at: Optional[datetime] = None
    cart_products: Optional[CartProductModel] = None

    class Config:
        orm_mode = True

class CartResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[CartModel] = None

    class Config:
        orm_mode = True

class CreateCartModel(BaseModel):
    total_amount: float
    products: List[CartProductModel] = None

    class Config:
        orm_mode = True

class AddCartProductModel(BaseModel):
    cart_id: int
    products: List[CartProductModel]

    class Config:
        orm_mode = True

class RemoveCartProductModel(BaseModel):
    cart_id: int
    product_ids: List[int]

    class Config:
        orm_mode = True

class OrderStatData(BaseModel):
    total_order: Optional[int] = 0
    pending_order: Optional[int] = 0
    completed_order: Optional[int] = 0
    failed_order: Optional[int] = 0

    class Config:
        orm_mode = True

class OrderStatResponse(BaseModel):
    status: bool
    message: str
    data: Optional[OrderStatData] = None

    class Config:
        orm_mode = True