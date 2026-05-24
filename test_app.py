import app

client = app.app.test_client()

def test_get_inventory():
    res = client.get("/inventory")
    assert res.status_code == 200

def test_add_item():
    res = client.post("/inventory", json={
        "product_name": "Test Product",
        "price": 10,
        "stock": 5
    })
    assert res.status_code == 201

def test_update_item():
    res = client.patch("/inventory/1", json={"price": 99})
    assert res.status_code in [200, 404]

def test_delete_item():
    res = client.delete("/inventory/1")
    assert res.status_code == 200