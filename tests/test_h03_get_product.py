import json  # noqa: F401


def test_h03_9siqt8tojo_cny_0001(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_6e92zmyyfz_czk_0002(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_hqtgwgpnh4_dkk_0003(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_oljcespc7z_eur_0004(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_66vchsjnup_gbp_0005(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_1ymwwn1n4o_hkd_0006(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_l9ecav7kim_hrk_0007(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_2zyfj3gm2n_huf_0008(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_0puk6v6ev0_idr_0009(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_ls4psxunum_ils_0010(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_9siqt8tojo_inr_0011(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_6e92zmyyfz_isk_0012(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_hqtgwgpnh4_jpy_0013(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_oljcespc7z_krw_0014(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_66vchsjnup_mxn_0015(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_1ymwwn1n4o_myr_0016(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_l9ecav7kim_nok_0017(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_2zyfj3gm2n_nzd_0018(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_0puk6v6ev0_php_0019(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_ls4psxunum_pln_0020(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_9siqt8tojo_ron_0021(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_6e92zmyyfz_rub_0022(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_hqtgwgpnh4_sek_0023(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_oljcespc7z_sgd_0024(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_66vchsjnup_thb_0025(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_1ymwwn1n4o_try_0026(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_l9ecav7kim_usd_0027(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 21
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_2zyfj3gm2n_zar_0028(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_0puk6v6ev0_aud_0029(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_ls4psxunum_bgn_0030(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_9siqt8tojo_brl_0031(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_6e92zmyyfz_cad_0032(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_hqtgwgpnh4_chf_0033(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_oljcespc7z_cny_0034(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_66vchsjnup_czk_0035(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_1ymwwn1n4o_dkk_0036(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_l9ecav7kim_eur_0037(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_2zyfj3gm2n_gbp_0038(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_0puk6v6ev0_hkd_0039(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_ls4psxunum_hrk_0040(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_9siqt8tojo_huf_0041(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_6e92zmyyfz_idr_0042(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_hqtgwgpnh4_ils_0043(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_oljcespc7z_inr_0044(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_66vchsjnup_isk_0045(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_1ymwwn1n4o_jpy_0046(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_l9ecav7kim_krw_0047(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_2zyfj3gm2n_mxn_0048(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_0puk6v6ev0_myr_0049(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_ls4psxunum_nok_0050(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_9siqt8tojo_nzd_0051(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_6e92zmyyfz_php_0052(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_hqtgwgpnh4_pln_0053(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_oljcespc7z_ron_0054(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_66vchsjnup_rub_0055(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_1ymwwn1n4o_sek_0056(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_l9ecav7kim_sgd_0057(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_2zyfj3gm2n_thb_0058(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_0puk6v6ev0_try_0059(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_ls4psxunum_usd_0060(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 57
    assert product["priceUsd"]["nanos"] == 80000000


def test_h03_9siqt8tojo_zar_0061(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_6e92zmyyfz_aud_0062(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_hqtgwgpnh4_bgn_0063(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_oljcespc7z_brl_0064(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_66vchsjnup_cad_0065(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_1ymwwn1n4o_chf_0066(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_l9ecav7kim_cny_0067(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_2zyfj3gm2n_czk_0068(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_0puk6v6ev0_dkk_0069(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_ls4psxunum_eur_0070(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_9siqt8tojo_gbp_0071(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_6e92zmyyfz_hkd_0072(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_hqtgwgpnh4_hrk_0073(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_oljcespc7z_huf_0074(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_66vchsjnup_idr_0075(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_1ymwwn1n4o_ils_0076(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_l9ecav7kim_inr_0077(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_2zyfj3gm2n_isk_0078(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_0puk6v6ev0_jpy_0079(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_ls4psxunum_krw_0080(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_9siqt8tojo_mxn_0081(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_6e92zmyyfz_myr_0082(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_hqtgwgpnh4_nok_0083(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_oljcespc7z_nzd_0084(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_66vchsjnup_php_0085(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_1ymwwn1n4o_pln_0086(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_l9ecav7kim_ron_0087(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_2zyfj3gm2n_rub_0088(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_0puk6v6ev0_sek_0089(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_ls4psxunum_sgd_0090(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_9siqt8tojo_thb_0091(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_6e92zmyyfz_try_0092(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_hqtgwgpnh4_usd_0093(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 0
    assert product["priceUsd"]["nanos"] == 990000000


def test_h03_oljcespc7z_zar_0094(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_66vchsjnup_aud_0095(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_1ymwwn1n4o_bgn_0096(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_l9ecav7kim_brl_0097(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_2zyfj3gm2n_cad_0098(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_0puk6v6ev0_chf_0099(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_ls4psxunum_cny_0100(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_9siqt8tojo_czk_0101(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_6e92zmyyfz_dkk_0102(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_hqtgwgpnh4_eur_0103(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_oljcespc7z_gbp_0104(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_66vchsjnup_hkd_0105(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_1ymwwn1n4o_hrk_0106(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_l9ecav7kim_huf_0107(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_2zyfj3gm2n_idr_0108(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_0puk6v6ev0_ils_0109(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_ls4psxunum_inr_0110(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_9siqt8tojo_isk_0111(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_6e92zmyyfz_jpy_0112(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_hqtgwgpnh4_krw_0113(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_oljcespc7z_mxn_0114(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_66vchsjnup_myr_0115(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_1ymwwn1n4o_nok_0116(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_l9ecav7kim_nzd_0117(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_2zyfj3gm2n_php_0118(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_0puk6v6ev0_pln_0119(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_ls4psxunum_ron_0120(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "RON"
