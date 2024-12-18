from flask import Blueprint, jsonify
from models import Goods,Order
from .base import api_bp

@api_bp.route("/good_of_numberpiece", methods=["GET"])
def good_of_numberpiece():
    try:
        # Goodsテーブルから全てのデータを取得
        goods = Goods.select()
        orders = Order.select()
    except Exception as e:
        # データベースエラーの場合は適切なレスポンスを返す
        return jsonify({"error": "Database query failed", "details": str(e)}), 500

   # 各商品IDの個数をカウント
    id_count = {}
    for order in orders:
        # id_countにgood.idが存在しなければ0を初期値として累積
        id_count[order.good.id] = id_count.get(order.good.id, 0) + 1

    # 商品データに売上個数を追加
    goods_data = []
    seen_ids = set()  # 同じ商品IDのデータを重複させないために使用
    for good in goods:
        if good.id not in seen_ids:
            goods_data.append({
                "id": good.id,
                "name": good.name,
                "price": good.price,
                "sales_count": id_count[good.id]
            })
            seen_ids.add(good.id)  # 重複を防ぐ

    # デバッグ用の出力
    print("ID Count:", id_count)
    print("Goods Data:", goods_data)

    return  jsonify(goods_data)
