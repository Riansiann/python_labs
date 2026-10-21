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

