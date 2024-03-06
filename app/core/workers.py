from celery import Celery

from app.core.constants import(
    CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND
)

celery_app = Celery(
    'jobs',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

@celery_app.task
def stock_alert(product_id: str, stock: int) -> dict:
    if stock < 10:
        return f"Alert: Stock for product {product_id} is low ({stock})"
    
    return f"Stock for product {product_id} is correct because stock is greater than or equal to 10"


if __name__ == '__main__':
    celery_app.start()
