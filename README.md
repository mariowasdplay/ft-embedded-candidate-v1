# Функциональное тестирование embedded-candidate-v1

Практикум 2026. Объект: `candidate(items, promo, fulfillment)` в `lab.py`, версия embedded-candidate-v1.

## Состав

- `lab.py` — исходный кандидат, **не изменялся**.
- `runner.py` — прогон 12 случаев, пишет `evidence/run.log` в UTF-8.
- `split.py` — нарезает `run.log` на `evidence/C01.txt … C06R.txt`.
- `report.md` — отчёт (паспорт, область, матрица случаев, дефекты, проверка ИИ, заключение).
- `data/catalog.csv` — каталог из задания.
- `data/cases.csv` — входы и ожидания по правилам.
- `evidence/` — фактические результаты прогона и ответ ИИ.
- `evidence/ai/prompt.txt`, `evidence/ai/response.txt` — запрос и ответ ИИ.

## Как воспроизвести

Требуется Python 3.10+ (стандартная библиотека, сеть не нужна).

    python runner.py
    python split.py
    python lab.py > evidence/C00.txt

Файлы `evidence/C01.txt … C06R.txt` перезапишутся теми же значениями.

## Ограничения варианта

Встроенный вариант: нет reference, нет R-SORT, нет UI/API/БД/платежей.
Вывод ограничен CLI-функцией расчёта корзины.