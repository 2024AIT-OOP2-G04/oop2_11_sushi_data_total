from flask import Blueprint, render_template, request, redirect, url_for
from models import Customer
import json

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/number_of_usage_by_table", methods=["GET"])
def number_of_usage_by_table():
    customers = Customer.select()
    print("data", customers)
    data = [{"id": customer.id, "table": customer.table} for customer in customers]
    return json.dumps(data)
