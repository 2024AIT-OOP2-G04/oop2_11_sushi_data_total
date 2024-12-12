from flask import Blueprint, render_template, request, redirect, url_for
from models import Order
import json

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/sales_by_good", methods=["GET"])
def number_of_usage_by_table():
    orders = Order.select()
    print("data", orders)
    data = [{"id": order.id, "goodsid": order.good.id,"goodsprice":order.good.price} for order in orders]
    return json.dumps(data)