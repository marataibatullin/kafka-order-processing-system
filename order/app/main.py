from app.routers.order import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "order-service"}
