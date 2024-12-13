from flask import Blueprint, render_template, request, redirect, url_for
from models import Order
import json

from .base import api_bp

@api_bp.route("/sales_by_day", methods=["GET"])
def sales_by_day():
    orders = Order.select()
    print("data", orders)
    data = [{"id": order.id, "date": order.order_date} for order in orders]
    print("data", data)
    return json.dumps(data)