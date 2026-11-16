import json  # noqa: F401


def test_h06_2zyfj3gm2n_x1_0001(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 2)]


def test_h06_0puk6v6ev0_x2_0002(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h06_ls4psxunum_x3_0003(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 6)]


def test_h06_9siqt8tojo_x4_0004(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 8)]


def test_h06_6e92zmyyfz_x5_0005(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 10)]


def test_h06_hqtgwgpnh4_x10_0006(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 20)]


def test_h06_oljcespc7z_x1_0007(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 2)]


def test_h06_66vchsjnup_x2_0008(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h06_1ymwwn1n4o_x3_0009(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 6)]


def test_h06_l9ecav7kim_x4_0010(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 8)]


def test_h06_2zyfj3gm2n_x5_0011(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 10)]


def test_h06_0puk6v6ev0_x10_0012(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 20)]


def test_h06_ls4psxunum_x1_0013(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 2)]


def test_h06_9siqt8tojo_x2_0014(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 4)]


def test_h06_6e92zmyyfz_x3_0015(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 6)]


def test_h06_hqtgwgpnh4_x4_0016(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 8)]


def test_h06_oljcespc7z_x5_0017(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 10)]


def test_h06_66vchsjnup_x10_0018(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 20)]


def test_h06_1ymwwn1n4o_x1_0019(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 2)]


def test_h06_l9ecav7kim_x2_0020(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h06_2zyfj3gm2n_x3_0021(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 6)]


def test_h06_0puk6v6ev0_x4_0022(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 8)]


def test_h06_ls4psxunum_x5_0023(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 10)]


def test_h06_9siqt8tojo_x10_0024(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 20)]


def test_h06_6e92zmyyfz_x1_0025(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 2)]


def test_h06_hqtgwgpnh4_x2_0026(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h06_oljcespc7z_x3_0027(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 6)]


def test_h06_66vchsjnup_x4_0028(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 8)]


def test_h06_1ymwwn1n4o_x5_0029(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 10)]


def test_h06_l9ecav7kim_x10_0030(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 20)]


def test_h06_2zyfj3gm2n_x1_0031(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 2)]


def test_h06_0puk6v6ev0_x2_0032(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h06_ls4psxunum_x3_0033(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 6)]


def test_h06_9siqt8tojo_x4_0034(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 8)]


def test_h06_6e92zmyyfz_x5_0035(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 10)]


def test_h06_hqtgwgpnh4_x10_0036(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 20)]


def test_h06_oljcespc7z_x1_0037(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 2)]


def test_h06_66vchsjnup_x2_0038(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h06_1ymwwn1n4o_x3_0039(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 6)]


def test_h06_l9ecav7kim_x4_0040(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 8)]


def test_h06_2zyfj3gm2n_x5_0041(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 10)]


def test_h06_0puk6v6ev0_x10_0042(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 20)]


def test_h06_ls4psxunum_x1_0043(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 2)]


def test_h06_9siqt8tojo_x2_0044(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 4)]


def test_h06_6e92zmyyfz_x3_0045(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 6)]


def test_h06_hqtgwgpnh4_x4_0046(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 8)]


def test_h06_oljcespc7z_x5_0047(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 10)]


def test_h06_66vchsjnup_x10_0048(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 20)]


def test_h06_1ymwwn1n4o_x1_0049(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 2)]


def test_h06_l9ecav7kim_x2_0050(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h06_2zyfj3gm2n_x3_0051(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 6)]


def test_h06_0puk6v6ev0_x4_0052(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 8)]


def test_h06_ls4psxunum_x5_0053(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 10)]


def test_h06_9siqt8tojo_x10_0054(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 20)]


def test_h06_6e92zmyyfz_x1_0055(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 2)]


def test_h06_hqtgwgpnh4_x2_0056(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h06_oljcespc7z_x3_0057(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 6)]


def test_h06_66vchsjnup_x4_0058(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 8)]


def test_h06_1ymwwn1n4o_x5_0059(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 10)]


def test_h06_l9ecav7kim_x10_0060(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 20)]


def test_h06_2zyfj3gm2n_x1_0061(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 2)]


def test_h06_0puk6v6ev0_x2_0062(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h06_ls4psxunum_x3_0063(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 6)]


def test_h06_9siqt8tojo_x4_0064(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 8)]


def test_h06_6e92zmyyfz_x5_0065(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 10)]


def test_h06_hqtgwgpnh4_x10_0066(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 20)]


def test_h06_oljcespc7z_x1_0067(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 2)]


def test_h06_66vchsjnup_x2_0068(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h06_1ymwwn1n4o_x3_0069(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 6)]


def test_h06_l9ecav7kim_x4_0070(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 8)]


def test_h06_2zyfj3gm2n_x5_0071(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 10)]


def test_h06_0puk6v6ev0_x10_0072(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 20)]


def test_h06_ls4psxunum_x1_0073(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 2)]


def test_h06_9siqt8tojo_x2_0074(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 4)]


def test_h06_6e92zmyyfz_x3_0075(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 6)]


def test_h06_hqtgwgpnh4_x4_0076(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 8)]


def test_h06_oljcespc7z_x5_0077(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 10)]


def test_h06_66vchsjnup_x10_0078(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 20)]


def test_h06_1ymwwn1n4o_x1_0079(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 2)]


def test_h06_l9ecav7kim_x2_0080(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h06_2zyfj3gm2n_x3_0081(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 6)]


def test_h06_0puk6v6ev0_x4_0082(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 8)]


def test_h06_ls4psxunum_x5_0083(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 10)]


def test_h06_9siqt8tojo_x10_0084(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 20)]


def test_h06_6e92zmyyfz_x1_0085(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 2)]


def test_h06_hqtgwgpnh4_x2_0086(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h06_oljcespc7z_x3_0087(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 6)]


def test_h06_66vchsjnup_x4_0088(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 8)]


def test_h06_1ymwwn1n4o_x5_0089(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 10)]


def test_h06_l9ecav7kim_x10_0090(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 20)]


def test_h06_2zyfj3gm2n_x1_0091(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 2)]


def test_h06_0puk6v6ev0_x2_0092(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h06_ls4psxunum_x3_0093(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 6)]


def test_h06_9siqt8tojo_x4_0094(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 8)]


def test_h06_6e92zmyyfz_x5_0095(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 10)]


def test_h06_hqtgwgpnh4_x10_0096(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 20)]


def test_h06_oljcespc7z_x1_0097(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 2)]


def test_h06_66vchsjnup_x2_0098(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h06_1ymwwn1n4o_x3_0099(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 6)]


def test_h06_l9ecav7kim_x4_0100(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 8)]
