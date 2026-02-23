from app.events.producer import publish_event
from app.schemas.order import OrderCreateInput, OrderResponseOutput
from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.post(
    "/order",
    response_model=OrderResponseOutput,
    status_code=status.HTTP_201_CREATED,
)
async def produce_event(request: OrderCreateInput):
    """Создание нового заказа"""

    topic = "orders"

    try:
        order_data = request.model_dump()

        publish_event(topic=topic, value=order_data)

        return {"status": "success", "message": f"Event published to topic '{topic}'", "data": {**order_data}}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to produce event: {str(e)}")
