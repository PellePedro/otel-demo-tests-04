import json  # noqa: F401


def test_h08_2zyfj3gm2n_0001(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0002(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0003(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0004(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0005(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0006(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0007(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0008(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0009(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_l9ecav7kim_0010(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_2zyfj3gm2n_0011(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0012(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0013(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0014(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0015(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0016(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0017(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0018(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0019(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_l9ecav7kim_0020(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_2zyfj3gm2n_0021(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0022(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0023(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0024(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0025(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0026(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0027(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0028(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0029(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_l9ecav7kim_0030(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_2zyfj3gm2n_0031(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0032(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0033(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0034(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0035(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0036(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0037(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0038(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0039(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_l9ecav7kim_0040(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_2zyfj3gm2n_0041(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0042(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0043(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0044(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0045(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0046(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0047(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0048(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0049(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_l9ecav7kim_0050(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_2zyfj3gm2n_0051(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0052(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0053(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0054(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0055(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0056(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0057(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0058(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0059(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_l9ecav7kim_0060(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_2zyfj3gm2n_0061(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0062(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0063(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0064(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0065(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0066(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0067(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0068(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0069(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_l9ecav7kim_0070(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_2zyfj3gm2n_0071(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0072(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0073(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0074(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0075(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0076(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0077(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0078(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0079(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_l9ecav7kim_0080(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_2zyfj3gm2n_0081(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0082(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0083(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0084(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0085(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0086(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0087(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0088(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0089(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_l9ecav7kim_0090(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_2zyfj3gm2n_0091(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0092(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0093(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0094(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0095(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0096(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0097(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0098(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0099(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_l9ecav7kim_0100(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []
