import json
import io
import contextlib

with contextlib.redirect_stdout(io.StringIO()):
    from lab import candidate

CASES = [
    ("C01",  {"B3000": 1}, "", "delivery"),
    ("C02",  {"B3000": 1}, "", "pickup"),
    ("C03",  {"LOW": 1}, "", "delivery"),
    ("C04",  {"HIGH": 1}, "", "delivery"),
    ("C05",  {"E3000": 1}, "STUDY10", "delivery"),
    ("C06",  {"E10005": 1}, "STUDY10", "delivery"),
    ("C07",  {"E10005": 1, "N200": 1}, "STUDY10", "delivery"),
    ("C08",  {"S2": 2}, "", "delivery"),
    ("C09",  {"S2": 3}, "", "delivery"),
    ("C10",  {"S2": 2}, "", "pickup"),
    ("C01R", {"B3000": 1}, "", "delivery"),
    ("C06R", {"E10005": 1}, "STUDY10", "delivery"),
]

lines = []
for cid, items, promo, ful in CASES:
    out = candidate(items, promo, ful)
    lines.append(json.dumps({
        "id": cid,
        "version": "embedded-candidate-v1",
        "input": {"items": items, "promo": promo, "fulfillment": ful},
        "actual": out,
    }, ensure_ascii=False))

with open("evidence/run.log", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print("wrote evidence/run.log with", len(lines), "cases")