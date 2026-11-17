from datetime import date
import re

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")

def make_student(fio, birthdate, group, gpa) -> dict:
    """Create and return a student record with validated data."""
    rec = {
        "fio": fio,
        "birthdate": birthdate,
        "group": group,
        "gpa": gpa
    }

    validate_student(rec)
    rec["gpa"] = float(rec["gpa"])
    
    return rec

def validate_student(rec) -> None:
    """
    Check the student record's fields, types, and values.
    Raise an exception if any data is invalid.
    """
    if not isinstance(rec, dict):
        raise ValueError("not a dict")
    
    keys = set(rec.keys())
    required_keys = set(STUDENT_FIELDS)

    # keys checking
    if keys != required_keys:
        missing = required_keys - keys
        extra = keys - required_keys
        raise ValueError(f"invalid keys: missing {missing}, extra {extra}")

    fio, group, birthdate, gpa = rec["fio"], rec["group"], rec["birthdate"], rec["gpa"]

    #fio checking
    if not isinstance(fio, str):
        raise TypeError("fio must be a string")
    if not fio.strip():
        raise ValueError("fio must not be empty")
    fio_list = [part for part in fio.split()]
    if not 2 <= len(fio_list) <= 3:
        raise ValueError("fio must contain 2 or 3 parts")

    # group checking
    if not isinstance(group, str):
            raise TypeError("group must be a string")
    if not group.strip():
        raise ValueError("group must not be empty")
        
    # birthdate checking
    if not isinstance(birthdate, str):
        raise TypeError("birthdate must be a string")
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", birthdate):
        raise ValueError("birthdate must be in YYYY-MM-DD format")
    try:
        birthdate = date.fromisoformat(birthdate)
    except ValueError as e:
        raise ValueError(f"invalid birthdate: {birthdate}") from e
    if birthdate > date.today():
        raise ValueError("birthdate cannot be in the future")

    # gpa checking
    gpa = rec["gpa"]
    if not isinstance(gpa, (int, float)) or isinstance(gpa, bool):
        raise TypeError("gpa must be a number")
    if not (0 <= gpa <= 5):
        raise ValueError("gpa must be between 0 and 5")


def student_age(rec, today=None) -> int:
    """
    Calculate the student's full age as of the given date.
    Use the current date if no date is provided.
    """
    validate_student(rec)
    birthdate = date.fromisoformat(rec["birthdate"])

    if isinstance(today, str):
        today = date.fromisoformat(today)
    if today is None:
        today = date.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

def format_student(rec):
    """Return a formatted string with the student's name, group, age, and GPA."""
    validate_student(rec)

    fio, group, gpa = rec["fio"], rec["group"], rec["gpa"]

    fio_list = list(fio.split())
    name = f"{fio_list[0].capitalize()} {"".join(f"{x[0].upper()}." for x in fio_list[1:])}"

    group = f"({group.strip().upper()})"

    age = student_age(rec)

    gpa = f"{gpa:.2f}"

    return f"{name} {group}, {age} лет, GPA: {gpa}"

def student_to_dict(rec):
    """Return an independent dictionary copy of a student record."""
    validate_student(rec)
    new_rec = {
        "fio": rec["fio"],
        "birthdate": rec["birthdate"],
        "group": rec["group"],
        "gpa": rec["gpa"]
    }

    return new_rec


def student_from_dict(d):
    """
    Create a student record from a dictionary.
    Validate the data and convert GPA to float.
    """

    if not isinstance(d, dict):
        raise ValueError("not a dict")
    if set(d.keys()) != set(STUDENT_FIELDS):
        raise ValueError(f"invalid keys: {set(d.keys())} != {set(STUDENT_FIELDS)}")

    raw_gpa = d["gpa"]

    if isinstance(raw_gpa, bool):
        raise ValueError("gpa must not be bool")
    try:
        gpa = float(raw_gpa)
    except (ValueError, TypeError) as e:
        raise ValueError(f"gpa must be a number, got {raw_gpa}") from e

    d_student = make_student(d["fio"], d["birthdate"], d["group"], gpa)

    return d_student


def update_student(rec, **fields):
    """Return a new student record with updated fields."""
    validate_student(rec)

    for key in fields:
        if  key not in STUDENT_FIELDS:
            raise KeyError(f"unknown key provided: {key}")

    new_rec = rec.copy()
    new_rec.update(fields)

    validate_student(new_rec)
    return new_rec
    