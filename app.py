from flask import Flask, request, jsonify
from models import inventory
from services import fetch_product

app = Flask(__name__)

# GET all inventory
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)

# GET single item
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return {"error": "Item not found"}, 404
    return jsonify(item)

# POST add item
@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.json

    new_item = {
        "id": len(inventory) + 1,
        "product_name": data["product_name"],
        "brand": data.get("brand", ""),
        "price": data.get("price", 0),
        "stock": data.get("stock", 0),
        "barcode": data.get("barcode", ""),
        "openfoodfacts": {}
    }

    inventory.append(new_item)
    return jsonify(new_item), 201

# PATCH update item
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)

    if not item:
        return {"error": "Item not found"}, 404

    data = request.json
    item.update(data)

    return jsonify(item)

# DELETE item
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global inventory
    inventory = [i for i in inventory if i["id"] != item_id]
    return {"message": "Item deleted"}, 200

# External API route
@app.route("/inventory/enrich/<barcode>", methods=["GET"])
def enrich_product(barcode):
    product = fetch_product(barcode)

    if not product:
        return {"error": "Product not found"}, 404

    return jsonify(product)

if __name__ == "__main__":
    app.run(debug=True)