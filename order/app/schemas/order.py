from pydantic import BaseModel


class OrderCreateInput(BaseModel):
    """Модель для создания заказа"""

    order_id: int
    user_id: int
    item: str
    quantity: int


class OrderResponseOutput(BaseModel):
    """Модель ответа при создании заказа"""

    status: str
    message: str
    data: dict
