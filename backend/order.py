"""In-memory order model and lifecycle operations for the prototype."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from threading import RLock
from uuid import uuid4

_STATUSES = {"placed", "accepted", "preparing", "ready", "out_for_delivery", "delivered", "cancelled"}
_ORDERS: dict[str, "Order"] = {}
_LOCK = RLock()

@dataclass
class Order:
    order_id: str
    student_id: str
    items: list[dict]
    total_price: float
    status: str = "placed"

    @classmethod
    def create(cls, student_id: str, items: list[dict]) -> "Order":
        if not student_id.strip() or not items:
            raise ValueError("Student ID and at least one item are required")
        total = 0.0
        clean = []
        for item in items:
            quantity = int(item.get("quantity", 1))
            if quantity < 1 or float(item["price"]) < 0:
                raise ValueError("Item quantity must be positive and price nonnegative")
            clean.append({"id": str(item["id"]), "name": str(item["name"]), "price": round(float(item["price"]), 2), "quantity": quantity})
            total += float(item["price"]) * quantity
        order = cls(str(uuid4()), student_id.strip(), clean, round(total, 2))
        with _LOCK:
            _ORDERS[order.order_id] = order
        return order

def update_order_status(order_id: str, new_status: str) -> Order:
    """Update an existing order using a known lifecycle status."""
    if new_status not in _STATUSES:
        raise ValueError(f"Status must be one of: {', '.join(sorted(_STATUSES))}")
    with _LOCK:
        if order_id not in _ORDERS:
            raise KeyError("Order not found")
        _ORDERS[order_id].status = new_status
        return _ORDERS[order_id]

def get_order(order_id: str) -> Order | None:
    with _LOCK:
        return _ORDERS.get(order_id)

def list_orders() -> list[Order]:
    with _LOCK:
        return list(_ORDERS.values())

def serialize_order(order: Order) -> dict:
    return asdict(order)