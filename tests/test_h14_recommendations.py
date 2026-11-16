import json  # noqa: F401


def test_h14_2zyfj3gm2n_inr_0001(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_isk_0002(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_jpy_0003(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_krw_0004(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_mxn_0005(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_myr_0006(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]


def test_h14_oljcespc7z_nok_0007(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_nzd_0008(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_php_0009(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_pln_0010(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_ron_0011(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_rub_0012(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_sek_0013(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_sgd_0014(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_thb_0015(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_try_0016(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]


def test_h14_oljcespc7z_usd_0017(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_zar_0018(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_aud_0019(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_bgn_0020(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_brl_0021(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_cad_0022(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_chf_0023(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_cny_0024(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_czk_0025(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]
