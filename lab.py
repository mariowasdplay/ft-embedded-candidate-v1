import json
DATA = {
    "B3000": (300000, 10, False), "E3000": (300000, 10, True),
    "E10005": (10005, 10, True), "N200": (20000, 10, False),
    "LOW": (299999, 10, False), "HIGH": (300001, 10, False),
    "S2": (15000, 2, True), "ZERO": (90000, 0, True)
}
def candidate(items, promo, fulfillment):
    if not isinstance(promo, str):
        return {"error": "PROMO"}
    code = promo.strip().upper()
    if code not in ("", "STUDY10"):
        return {"error": "PROMO"}
    if fulfillment not in ("delivery", "pickup"):
        return {"error": "FULFILLMENT"}
    if not items:
        return {"error": "EMPTY_CART"}
    subtotal = eligible = 0
    for product_id, q in items.items():
        if product_id not in DATA:
            return {"error": "PRODUCT"}
        if type(q) is not int or not 1 <= q <= 10:
            return {"error": "QUANTITY"}
        price, stock, participates = DATA[product_id]
        subtotal += price * q
        if participates:
            eligible += price * q
    discount = eligible // 10 if code else 0
    after_discount = subtotal - discount
    delivery = 0 if fulfillment == "pickup" or after_discount > 300000 else 29900
    return {"subtotal": subtotal, "eligible_subtotal": eligible,
            "discount": discount, "after_discount": after_discount,
            "delivery": delivery, "total": after_discount + delivery}
items = {"B3000": 1}
promo = ""
fulfillment = "delivery"
print(json.dumps({"version": "embedded-candidate-v1", "input": {
    "items": items, "promo": promo, "fulfillment": fulfillment},
    "actual": candidate(items, promo, fulfillment)}, ensure_ascii=False, indent=2))
