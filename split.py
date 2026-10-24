import json
import pathlib

path = pathlib.Path("evidence/run.log")
raw = path.read_bytes()

# Страховка: UTF-16 с BOM или UTF-8 с BOM или обычный UTF-8
for enc in ("utf-8-sig", "utf-16", "utf-8"):
    try:
        text = raw.decode(enc)
        break
    except UnicodeDecodeError:
        continue
else:
    raise SystemExit("не удалось декодировать run.log")

dec = json.JSONDecoder()
idx = 0
count = 0
while True:
    while idx < len(text) and text[idx] in " \t\r\n":
        idx += 1
    if idx >= len(text):
        break
    obj, idx = dec.raw_decode(text, idx)
    name = obj.get("id", "C00")
    pathlib.Path(f"evidence/{name}.txt").write_text(
        json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    count += 1

print(f"written {count} files")