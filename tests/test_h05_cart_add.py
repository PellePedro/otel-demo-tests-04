import json  # noqa: F401


def test_h05_2zyfj3gm2n_x5_0001(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 5)]


def test_h05_0puk6v6ev0_x10_0002(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 10)]


def test_h05_ls4psxunum_x1_0003(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 1)]


def test_h05_9siqt8tojo_x2_0004(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 2)]


def test_h05_6e92zmyyfz_x3_0005(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 3)]


def test_h05_hqtgwgpnh4_x4_0006(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h05_oljcespc7z_x5_0007(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 5)]


def test_h05_66vchsjnup_x10_0008(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 10)]


def test_h05_1ymwwn1n4o_x1_0009(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 1)]


def test_h05_l9ecav7kim_x2_0010(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 2)]


def test_h05_2zyfj3gm2n_x3_0011(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 3)]


def test_h05_0puk6v6ev0_x4_0012(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h05_ls4psxunum_x5_0013(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 5)]


def test_h05_9siqt8tojo_x10_0014(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 10)]


def test_h05_6e92zmyyfz_x1_0015(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 1)]


def test_h05_hqtgwgpnh4_x2_0016(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 2)]


def test_h05_oljcespc7z_x3_0017(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 3)]


def test_h05_66vchsjnup_x4_0018(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h05_1ymwwn1n4o_x5_0019(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 5)]


def test_h05_l9ecav7kim_x10_0020(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 10)]


def test_h05_2zyfj3gm2n_x1_0021(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 1)]


def test_h05_0puk6v6ev0_x2_0022(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 2)]


def test_h05_ls4psxunum_x3_0023(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 3)]


def test_h05_9siqt8tojo_x4_0024(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 4)]


def test_h05_6e92zmyyfz_x5_0025(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 5)]


def test_h05_hqtgwgpnh4_x10_0026(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 10)]


def test_h05_oljcespc7z_x1_0027(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 1)]


def test_h05_66vchsjnup_x2_0028(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 2)]


def test_h05_1ymwwn1n4o_x3_0029(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 3)]


def test_h05_l9ecav7kim_x4_0030(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h05_2zyfj3gm2n_x5_0031(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 5)]


def test_h05_0puk6v6ev0_x10_0032(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 10)]


def test_h05_ls4psxunum_x1_0033(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 1)]


def test_h05_9siqt8tojo_x2_0034(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 2)]


def test_h05_6e92zmyyfz_x3_0035(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 3)]


def test_h05_hqtgwgpnh4_x4_0036(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h05_oljcespc7z_x5_0037(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 5)]


def test_h05_66vchsjnup_x10_0038(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 10)]


def test_h05_1ymwwn1n4o_x1_0039(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 1)]


def test_h05_l9ecav7kim_x2_0040(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 2)]


def test_h05_2zyfj3gm2n_x3_0041(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 3)]


def test_h05_0puk6v6ev0_x4_0042(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h05_ls4psxunum_x5_0043(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 5)]


def test_h05_9siqt8tojo_x10_0044(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 10)]


def test_h05_6e92zmyyfz_x1_0045(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 1)]


def test_h05_hqtgwgpnh4_x2_0046(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 2)]


def test_h05_oljcespc7z_x3_0047(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 3)]


def test_h05_66vchsjnup_x4_0048(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h05_1ymwwn1n4o_x5_0049(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 5)]


def test_h05_l9ecav7kim_x10_0050(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 10)]


def test_h05_2zyfj3gm2n_x1_0051(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 1)]


def test_h05_0puk6v6ev0_x2_0052(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 2)]


def test_h05_ls4psxunum_x3_0053(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 3)]


def test_h05_9siqt8tojo_x4_0054(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 4)]


def test_h05_6e92zmyyfz_x5_0055(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 5)]


def test_h05_hqtgwgpnh4_x10_0056(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 10)]


def test_h05_oljcespc7z_x1_0057(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 1)]


def test_h05_66vchsjnup_x2_0058(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 2)]


def test_h05_1ymwwn1n4o_x3_0059(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 3)]


def test_h05_l9ecav7kim_x4_0060(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h05_2zyfj3gm2n_x5_0061(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 5)]


def test_h05_0puk6v6ev0_x10_0062(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 10)]


def test_h05_ls4psxunum_x1_0063(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 1)]


def test_h05_9siqt8tojo_x2_0064(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 2)]


def test_h05_6e92zmyyfz_x3_0065(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 3)]


def test_h05_hqtgwgpnh4_x4_0066(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h05_oljcespc7z_x5_0067(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 5)]


def test_h05_66vchsjnup_x10_0068(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 10)]


def test_h05_1ymwwn1n4o_x1_0069(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 1)]


def test_h05_l9ecav7kim_x2_0070(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 2)]


def test_h05_2zyfj3gm2n_x3_0071(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 3)]


def test_h05_0puk6v6ev0_x4_0072(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h05_ls4psxunum_x5_0073(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 5)]


def test_h05_9siqt8tojo_x10_0074(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 10)]


def test_h05_6e92zmyyfz_x1_0075(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 1)]


def test_h05_hqtgwgpnh4_x2_0076(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 2)]


def test_h05_oljcespc7z_x3_0077(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 3)]


def test_h05_66vchsjnup_x4_0078(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h05_1ymwwn1n4o_x5_0079(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 5)]


def test_h05_l9ecav7kim_x10_0080(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 10)]


def test_h05_2zyfj3gm2n_x1_0081(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 1)]


def test_h05_0puk6v6ev0_x2_0082(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 2)]


def test_h05_ls4psxunum_x3_0083(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 3)]


def test_h05_9siqt8tojo_x4_0084(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 4)]


def test_h05_6e92zmyyfz_x5_0085(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 5)]


def test_h05_hqtgwgpnh4_x10_0086(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 10)]


def test_h05_oljcespc7z_x1_0087(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 1)]


def test_h05_66vchsjnup_x2_0088(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 2)]


def test_h05_1ymwwn1n4o_x3_0089(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 3)]


def test_h05_l9ecav7kim_x4_0090(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h05_2zyfj3gm2n_x5_0091(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 5)]


def test_h05_0puk6v6ev0_x10_0092(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 10)]


def test_h05_ls4psxunum_x1_0093(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 1)]


def test_h05_9siqt8tojo_x2_0094(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 2)]


def test_h05_6e92zmyyfz_x3_0095(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 3)]


def test_h05_hqtgwgpnh4_x4_0096(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h05_oljcespc7z_x5_0097(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 5)]


def test_h05_66vchsjnup_x10_0098(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 10)]


def test_h05_1ymwwn1n4o_x1_0099(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 1)]


def test_h05_l9ecav7kim_x2_0100(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 2)]


def test_h05_2zyfj3gm2n_x3_0101(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 3)]


def test_h05_0puk6v6ev0_x4_0102(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h05_ls4psxunum_x5_0103(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 5)]


def test_h05_9siqt8tojo_x10_0104(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 10)]


def test_h05_6e92zmyyfz_x1_0105(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 1)]


def test_h05_hqtgwgpnh4_x2_0106(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 2)]


def test_h05_oljcespc7z_x3_0107(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 3)]


def test_h05_66vchsjnup_x4_0108(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h05_1ymwwn1n4o_x5_0109(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 5)]


def test_h05_l9ecav7kim_x10_0110(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 10)]


def test_h05_2zyfj3gm2n_x1_0111(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 1)]


def test_h05_0puk6v6ev0_x2_0112(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 2)]


def test_h05_ls4psxunum_x3_0113(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 3)]


def test_h05_9siqt8tojo_x4_0114(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 4)]


def test_h05_6e92zmyyfz_x5_0115(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 5)]


def test_h05_hqtgwgpnh4_x10_0116(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 10)]


def test_h05_oljcespc7z_x1_0117(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 1)]


def test_h05_66vchsjnup_x2_0118(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 2)]


def test_h05_1ymwwn1n4o_x3_0119(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 3)]


def test_h05_l9ecav7kim_x4_0120(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h05_2zyfj3gm2n_x5_0121(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 5)]


def test_h05_0puk6v6ev0_x10_0122(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 10)]


def test_h05_ls4psxunum_x1_0123(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 1)]


def test_h05_9siqt8tojo_x2_0124(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 2)]


def test_h05_6e92zmyyfz_x3_0125(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 3)]


def test_h05_hqtgwgpnh4_x4_0126(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h05_oljcespc7z_x5_0127(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 5)]


def test_h05_66vchsjnup_x10_0128(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 10)]


def test_h05_1ymwwn1n4o_x1_0129(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 1)]


def test_h05_l9ecav7kim_x2_0130(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 2)]


def test_h05_2zyfj3gm2n_x3_0131(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 3)]


def test_h05_0puk6v6ev0_x4_0132(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h05_ls4psxunum_x5_0133(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 5)]


def test_h05_9siqt8tojo_x10_0134(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 10)]


def test_h05_6e92zmyyfz_x1_0135(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 1)]


def test_h05_hqtgwgpnh4_x2_0136(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 2)]


def test_h05_oljcespc7z_x3_0137(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 3)]


def test_h05_66vchsjnup_x4_0138(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h05_1ymwwn1n4o_x5_0139(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 5)]


def test_h05_l9ecav7kim_x10_0140(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 10)]


def test_h05_2zyfj3gm2n_x1_0141(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 1)]


def test_h05_0puk6v6ev0_x2_0142(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 2)]


def test_h05_ls4psxunum_x3_0143(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 3)]


def test_h05_9siqt8tojo_x4_0144(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 4)]


def test_h05_6e92zmyyfz_x5_0145(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 5)]


def test_h05_hqtgwgpnh4_x10_0146(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 10)]


def test_h05_oljcespc7z_x1_0147(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 1)]


def test_h05_66vchsjnup_x2_0148(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 2)]


def test_h05_1ymwwn1n4o_x3_0149(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 3)]


def test_h05_l9ecav7kim_x4_0150(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h05_2zyfj3gm2n_x5_0151(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 5)]


def test_h05_0puk6v6ev0_x10_0152(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 10)]


def test_h05_ls4psxunum_x1_0153(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 1)]


def test_h05_9siqt8tojo_x2_0154(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 2)]


def test_h05_6e92zmyyfz_x3_0155(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 3)]


def test_h05_hqtgwgpnh4_x4_0156(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h05_oljcespc7z_x5_0157(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 5)]


def test_h05_66vchsjnup_x10_0158(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 10)]


def test_h05_1ymwwn1n4o_x1_0159(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 1)]


def test_h05_l9ecav7kim_x2_0160(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 2)]


def test_h05_2zyfj3gm2n_x3_0161(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 3)]


def test_h05_0puk6v6ev0_x4_0162(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h05_ls4psxunum_x5_0163(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 5)]


def test_h05_9siqt8tojo_x10_0164(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 10)]


def test_h05_6e92zmyyfz_x1_0165(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 1)]


def test_h05_hqtgwgpnh4_x2_0166(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 2)]


def test_h05_oljcespc7z_x3_0167(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 3)]


def test_h05_66vchsjnup_x4_0168(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h05_1ymwwn1n4o_x5_0169(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 5)]


def test_h05_l9ecav7kim_x10_0170(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 10)]


def test_h05_2zyfj3gm2n_x1_0171(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 1)]


def test_h05_0puk6v6ev0_x2_0172(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 2)]


def test_h05_ls4psxunum_x3_0173(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 3)]


def test_h05_9siqt8tojo_x4_0174(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 4)]


def test_h05_6e92zmyyfz_x5_0175(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 5)]


def test_h05_hqtgwgpnh4_x10_0176(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 10)]


def test_h05_oljcespc7z_x1_0177(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 1)]


def test_h05_66vchsjnup_x2_0178(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 2)]


def test_h05_1ymwwn1n4o_x3_0179(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 3)]


def test_h05_l9ecav7kim_x4_0180(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h05_2zyfj3gm2n_x5_0181(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 5)]


def test_h05_0puk6v6ev0_x10_0182(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 10)]


def test_h05_ls4psxunum_x1_0183(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 1)]


def test_h05_9siqt8tojo_x2_0184(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 2)]


def test_h05_6e92zmyyfz_x3_0185(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 3)]


def test_h05_hqtgwgpnh4_x4_0186(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h05_oljcespc7z_x5_0187(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 5)]


def test_h05_66vchsjnup_x10_0188(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 10)]


def test_h05_1ymwwn1n4o_x1_0189(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 1)]


def test_h05_l9ecav7kim_x2_0190(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 2)]


def test_h05_2zyfj3gm2n_x3_0191(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 3)]


def test_h05_0puk6v6ev0_x4_0192(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h05_ls4psxunum_x5_0193(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 5)]


def test_h05_9siqt8tojo_x10_0194(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 10)]


def test_h05_6e92zmyyfz_x1_0195(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 1)]


def test_h05_hqtgwgpnh4_x2_0196(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 2)]


def test_h05_oljcespc7z_x3_0197(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 3)]


def test_h05_66vchsjnup_x4_0198(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h05_1ymwwn1n4o_x5_0199(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 5)]


def test_h05_l9ecav7kim_x10_0200(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 10)]
