from collections import Counter
from flask import Blueprint, render_template, request, redirect, url_for
from models import Customer
import json

from .base import api_bp

@api_bp.route("/number_of_usage_by_table", methods=["GET"])
def number_of_usage_by_table():
    customers = Customer.select()
    print("data", customers)
    data = [{"id": customer.id, "table": customer.table} for customer in customers]
    table_data = [entry["table"] for entry in data]
    table_usage_count = Counter(table_data)
    total_usage_count = sum(table_usage_count.values())
    response_data = {
        "table_usage": sorted([{"table": table, "usage_count": count} for table, count in table_usage_count.items()],key=lambda x: x["table"]),
        "total_usage_count": total_usage_count
    }
    return json.dumps(response_data)
