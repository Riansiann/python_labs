from src.lab08.models import (
    make_student,
    validate_student,
    student_age,
    format_student,
    student_to_dict,
    student_from_dict
    )

from src.lab08.serialize import (
    students_to_json,
    students_from_json
    )

print("CREATE STUDENT")

student = make_student("Иванов Иван Иванович", "2007-05-14", "БИВТ-26-6-1", 4.3)
print(student)

validate_student(student)
print("\nVALIDATION PASSED")

print("\nAGE:", student_age(student))

print("\nFORMAT STUDENT")
print(format_student(student))

print("\nCOPY")
copied = student_to_dict(student)
print("Equal:", copied == student)
print("Same object:", copied is student)

print("\nFROM DICT")
data = student.copy()
data["gpa"] = "4.7"
restored = student_from_dict(student)
print(restored)

print("\nINVALID GPA")

try:
    make_student("Иванов Иван Иванович", "2007-05-14", "БИВТ", 7)
except ValueError as error:
    print("Expected error:", error)


print("\nREAD JSON")
students = students_from_json("data/lab08/students_input.json")

for s in students:
    print(format_student(s))

print("\nWRITE JSON")
students_to_json(students, "data/lab08/students_output.json")
print("JSON saved successfully")

print("\nINVALID JSON")
try:
    students_from_json("data/lab08/students_bad.json")
except ValueError as error:
    print("Expected error:", error)



