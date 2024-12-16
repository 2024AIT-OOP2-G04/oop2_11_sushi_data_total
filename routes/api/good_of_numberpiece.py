from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from models import Goods

from .base import api_bp

@api_bp.route("/good_of_numberpiece", methods=["GET"])
def good_of_numberpiece():
    # Goodsテーブルから全てのデータを取得
    goods = Goods.select()

    # データを辞書形式に変換（例：Goodsモデルに名前や価格などのフィールドがある場合）
    goods_data = [{"id": good.id, "name": good.name, "price": good.price} for good in goods]

    # デバッグ用の出力
    print("data", goods_data)

    # JSONレスポンスを返す
    return jsonify(goods_data)