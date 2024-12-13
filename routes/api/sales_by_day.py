from flask import Blueprint, render_template, request, redirect, url_for
from models import Order
import json

from .base import api_bp

@api_bp.route("/sales_by_day", methods=["GET"])
def sales_by_day():
    orders = Order.select()

    amount_data = [0,0,0,0,0,0,0]
    for element in orders:
        _weekday = element.order_date.weekday()
        amount_data[_weekday] += int(element.good.price)

    data = {
        "月曜日": amount_data[0],
        "火曜日": amount_data[1],
        "水曜日": amount_data[2],
        "木曜日": amount_data[3],
        "金曜日": amount_data[4],
        "土曜日": amount_data[5],
        "日曜日": amount_data[6],
    }

    return json.dumps(data , ensure_ascii=False)