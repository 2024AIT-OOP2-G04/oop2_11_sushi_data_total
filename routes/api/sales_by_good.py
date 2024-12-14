from flask import Blueprint, render_template, request, redirect, url_for
from models import Order
import json

from .base import api_bp


@api_bp.route("/sales_by_good", methods=["GET"])
def number_of_usage_by_table():
    orders = Order.select()
    print("data", orders)
    l=[]
    sumprice=[]
    for order in orders:
        if(l.count(order.good.id)<=0):
            l.append(order.good.id)
            sumprice.append(float(order.good.price))
        
        sumprice[l.index(order.good.id)]=sumprice[l.index(order.good.id)]+float(order.good.price)

    data = [{"id": order.id, "goodsid": order.good.id,"goodsprice":float(order.good.price)} for order in orders]
    return json.dumps(data)
