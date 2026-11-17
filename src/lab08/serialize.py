import json
import csv
from src.lab08.models import student_to_dict, student_from_dict


def students_to_json(students, path):
    """Save a list of validated student records to a JSON file."""
    data = [student_to_dict(s) for s in students]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def students_from_json(path):
    """
    Load and validate student records from a JSON file.
    Raise ValueError with the record number if any data is invalid.
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("JSON root must be an array")

    students = []

    for index, record in enumerate(data, start = 1):
        try:
            student = student_from_dict(record)
        except ValueError as e:
            raise ValueError(f"Invalid student record {index}: {e}") from e

        students.append(student)

    return students

def students_from_csv(path):
    students = []
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for i, row in enumerate(reader, start = 1):
            try:
                students.append(student_from_dict(row))
            except (ValueError, TypeError) as e:
                raise ValueError(f"invalid rec {i}: {e}") from e
    return students