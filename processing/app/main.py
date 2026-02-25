from consumer import consume_orders
from producer import publish_event


def process():
    for order in consume_orders():
        status = "confirmed" if order["quantity"] > 0 else "rejected"

        publish_event("notifications", {
            "order_id": order["order_id"],
            "status": status
        })

if __name__ == "__main__":
    process()