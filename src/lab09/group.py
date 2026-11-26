from pathlib import Path
import csv
import os

from src.lab08.models import student_from_dict, validate_student, STUDENT_FIELDS    


# utility functions
def ensure_storage(path):
    """Create a CSV storage file with a header if it does not exist."""
    path = Path(path)

    if path.exists():
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
        writer.writeheader()


def load_students(path) -> list[dict]:
    """Load and validate student records from a CSV file."""
    ensure_storage(path)

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError(f"file {path} must contain fieldnames")
        if tuple(reader.fieldnames) != STUDENT_FIELDS:
            raise ValueError(f"file {path} contains invalid fieldnames")

        students = []

        for number, row in enumerate(reader, start = 2):
            if None in row or None in row.values():
                raise ValueError(f"file {path} contains invalid data in line {number}: {row}")

            try:
                students.append(student_from_dict(row))
            except (ValueError, TypeError) as e:
                raise ValueError(f"It is impossible to load line {number}: {row}. Error: {e}") from e 

    return students 


def save_students(path, students):
    """Validate and save student records to a CSV file."""
    path = Path(path)
    ensure_storage(path)

    for student in students:
        validate_student(student)

    tmp_path = str(path) + ".tmp"
    
    try:
        with open(tmp_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
            writer.writeheader()
            writer.writerows(students)

        os.replace(tmp_path, path)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

# CRUD functions

def add_student(path, student):
    """Add a new student to the CSV storage."""
    validate_student(student)

    students = load_students(path)

    # existing student check
    for existing_student in students:
        if existing_student["fio"] == student["fio"]:
            raise ValueError("student with this fio already exists")
        
    students.append(dict(student))
    save_students(path, students)

def list_students(path, sort_by=None):
    """Return students optionally sorted by fio or gpa."""
    if sort_by not in (None, "fio", "gpa"):
            raise ValueError(f"{sort_by} is unknown sorting")
    
    students = load_students(path)

    if sort_by == "fio":
        return sorted(students, key=lambda s: s["fio"])
    if sort_by == "gpa":
        return sorted(students, key=lambda s: s["gpa"])
    
    return students

def find_students(path, substr):
    """Find students by a case-insensitive fio substring."""
    students = load_students(path)

    needle = substr.casefold()
    return [student for student in students 
            if needle in student["fio"].casefold()
            ]

def remove_student(path, fio):
    """Remove all students with the given fio and return their count."""
    students = load_students(path)

    remaining = [student for student in students 
                 if student["fio"] != fio
                 ]
    removed_num = len(students) - len(remaining)

    if removed_num > 0:
        save_students(path, remaining)
    return removed_num

def update_student(path, fio, **fields):
    """Update the first matching student record and return success status."""
    for key in fields:
        if key not in STUDENT_FIELDS:
            raise KeyError(f"unknown field '{key}'")

    students = load_students(path)
    for s_number, student in enumerate(students):
        if student["fio"] == fio:
            updated = dict(student)
            updated.update(fields)
            validate_student(updated)

            students[s_number] = updated
            save_students(path, students)
            return True
    return False


def stats(path, n = 5) -> dict:
    students = load_students(path)
    count = len(students)

    # counting min, max, avg gpa 
    gpa_list = [student["gpa"] for student in students]
    min_gpa, max_gpa = min(gpa_list), max(gpa_list)
    boundary_gpa = (min_gpa, max_gpa)
    avg_gpa = sum(boundary_gpa) / 2

    # create group list with number of students for each group
    groups = {}
    
    for student in students:
        group = student["group"]

        if groups.get(group) is None:
            groups[group] = 0
        groups[group] += 1

    # create a list of best students
    s_sort_gpa = sorted(students, key=lambda s: s["gpa"], reverse = True)

    best_students = []
    for student in s_sort_gpa[:n]:
        rec = {
            "fio": student["fio"],
            "gpa": student["gpa"]            
        }

        best_students.append(rec)

    stat_dict = {
        "count": count,
        "min_gpa": min_gpa,
        "max_gpa": max_gpa,
        "avg_gpa": avg_gpa, 
        "groups": groups,
        "top_students": best_students
    }

    return stat_dict

    








    


    

