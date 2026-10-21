# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX)
## Задание A — JSON ↔ CSV
### json_to_csv
Функция преобразует JSON-файл, содержащий список словарей, в CSV-таблицу. Данные считываются с помощью json.load(), после чего формируется список столбцов из всех уникальных ключей словарей в порядке их первого появления. Для записи используется csv.DictWriter. Если в словаре отсутствует какой-либо ключ, соответствующая ячейка заполняется пустой строкой (restval="").
```python
import json
import csv 
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Convert a JSON file to CSV.
    Support a list of dictionaries and fill missing fields with empty strings.
    Use UTF-8 encoding. Preserve column order based on the first
    appearance of keys across all dictionaries.
    """

    json_p = Path(json_path)

    if not json_p.is_file():
        raise FileNotFoundError("File not found")
    if json_p.suffix.lower() != ".json": 
        raise ValueError("File must have .json extension")

    with json_p.open("r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e.msg}, line {e.lineno}, column {e.colno}") from e

    if not isinstance(data, list):
        raise ValueError("JSON must contain a list")
    if not data:
        raise ValueError("JSON list must not be empty")
    for di in data:
        if not isinstance(di, dict):
            raise ValueError("Data's components must be dictionaries")
        for key in di.keys():
            if not isinstance(key, str):
                raise ValueError("Dictionaries' keys must be strings")
    fieldnames = []

    for di in data:
        for key in di:
            if key not in fieldnames:
                fieldnames.append(key)
    if not fieldnames:
        raise ValueError("Dictionary does not contain keys")

    csv_p = Path(csv_path)
    if csv_p.suffix.lower() != ".csv":
            raise ValueError("Output file must have .csv extension")
    
    csv_p.parent.mkdir(parents = True, exist_ok = True)
  
    with csv_p.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(data)
```
### csv_to_json
Функция преобразует CSV-таблицу в JSON-файл. Для чтения используется csv.DictReader, который формирует словари на основе заголовков таблицы. Полученный список словарей сохраняется с помощью json.dump() с параметрами ensure_ascii=False для сохранения кириллицы и indent=2 для форматирования.
```python
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Convert a CSV file to JSON (a list of dictionaries).
    Require headers and preserve CSV values as strings.
    Use json.dump(..., ensure_ascii=False, indent=2).
    """
    
    csv_p = Path(csv_path)

    if not csv_p.is_file():
        raise FileNotFoundError("File not found")
    if csv_p.suffix.lower() != ".csv":
        raise ValueError("File must have .csv extension")

    with csv_p.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        if not fieldnames:
            raise ValueError("CSV must contain headers")
        if any(not name or not name.strip() for name in fieldnames):
            raise ValueError("CSV headers must not be empty")
        if len(fieldnames) != len(set(fieldnames)):
            raise ValueError("CSV headers must be unique")

        rows =  list(reader)

    if not rows:
        raise ValueError("CSV must contain at least one data row")

    json_p = Path(json_path)

    if json_p.suffix.lower() != ".json":
            raise ValueError("Output file must have .json extension")
    json_p.parent.mkdir(parents = True, exist_ok = True)
    

    with json_p.open("w", encoding="utf-8") as file:
        json.dump(rows, file, ensure_ascii=False, indent=2)    

if __name__ == '__main__':
    csv_to_json(r'data\samples\people.csv',
                r'data\out\people_from_csv.json')
    json_to_csv(r'data\samples\people.json',
                r'data\out\people_from_json.csv')
```
### Запуск:
```python
python -m src.lab05.json_csv
```
### Преобразование `people.json` в `people_from_json.csv`:
![people_from_json](../../images/lab05/people_from_json.png)

### Преобразование `people.csv` в `people_from_csv.json`:
![people_from_csv](../../images/lab05/people_from_csv.png)

## Задание B — CSV → XLSX
Функция преобразует CSV-таблицу в Excel-файл формата XLSX с использованием библиотеки openpyxl. Данные считываются через csv.reader() и записываются на лист Sheet1 с помощью ws.append(). Ширина столбцов автоматически устанавливается по максимальной длине содержимого, но не менее 8 единиц.
```python
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Convert a CSV file to XLSX using openpyxl.
    Use the first CSV row as headers.
    Name the worksheet "Sheet1".
    Adjust column widths based on text length (minimum width of 8).
    """

    csv_p = Path(csv_path)
    if not csv_p.is_file():
        raise FileNotFoundError("File not found")
    if csv_p.suffix.lower() != ".csv":
        raise ValueError("File must have .csv extension")

    with csv_p.open("r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV file is empty")
    headers = rows[0]
    if not headers or any(not name.strip() for name in headers):
        raise ValueError("CSV headers must not be empty")
    if len(headers) != len(set(headers)):
        raise ValueError("CSV headers must be unique")
    if len(rows) < 2:
        raise ValueError("CSV must contain at least one data row")
    for row in rows:
        if len(row) != len(headers):
            raise ValueError("CSV file contains rows with missing or extra fields")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    for column in ws.columns:
        max_length = max(len(str(cell.value)) if cell.value is not None else 0 for cell in column)
        width = max(8, max_length)

        letter = get_column_letter(column[0].column)
        ws.column_dimensions[letter].width = width

    xlsx_p = Path(xlsx_path)
    if xlsx_p.suffix.lower() != ".xlsx":
            raise ValueError("Output file must have .xlsx extension")
    
    xlsx_p.parent.mkdir(parents=True, exist_ok=True)
 

    wb.save(xlsx_p)


if __name__ == '__main__':
    csv_to_xlsx(r"data/samples/people.csv", r"data/out/people.xlsx")
```
### Запуск:
```python
python -m src.lab05.csv_xlsx
```
### Создание `people.xlsx` из `people.csv`
![people.xlsx](../../images/lab05/people.png)

## Обработка ошибок

### json_to_csv()
    FileNotFoundError — входной JSON-файл не найден.
    ValueError — неверное расширение входного (.json) или выходного (.csv) файла.
    ValueError — некорректный синтаксис JSON. Перехватывается json.JSONDecodeError, после чего выводится сообщение с причиной ошибки, номером строки и столбца.
    ValueError — JSON содержит не список либо список пуст.
    ValueError — элементы списка не являются словарями.
    ValueError — ключи словарей не являются строками.
    ValueError — в словарях отсутствуют ключи для формирования заголовка CSV.

### csv_to_json()
    FileNotFoundError — входной CSV-файл не найден.
    ValueError — неверное расширение входного (.csv) или выходного (.json) файла.
    ValueError — CSV не содержит заголовков.
    ValueError — заголовки пустые или состоят только из пробельных символов.
    ValueError — названия столбцов повторяются.
    ValueError — CSV не содержит строк данных.

### csv_to_xlsx()
    FileNotFoundError — входной CSV-файл не найден.
    ValueError — неверное расширение входного (.csv) или выходного (.xlsx) файла.
    ValueError — входной CSV-файл пуст.
    ValueError — заголовки отсутствуют, пустые или состоят только из пробельных символов.
    ValueError — названия столбцов повторяются.
    ValueError — CSV не содержит хотя бы одной строки данных.
    ValueError — количество значений в строках не совпадает с количеством столбцов (лишние или отсутствующие поля).