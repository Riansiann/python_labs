import argparse
import sys
from pprint import pprint

from src.lab08.models import make_student, format_student
from src.lab09.group import (
    add_student,
    list_students,
    find_students,
    remove_student,
    update_student,
    stats
)

def build_parser():
    parser = argparse.ArgumentParser(description="CSV student storage")
    parser.add_argument("--db", default="data/lab09/students.csv", help="Path to the CSV file")
        
    sub = parser.add_subparsers(dest="command", required=True)

    add_parser = sub.add_parser("add", help="Add a new student.")
    add_parser.add_argument("--fio", required=True, help="Student's full name.")
    add_parser.add_argument("--birthdate", required=True, help="Birthdate in YYYY-MM-DD format.")
    add_parser.add_argument("--group", required=True, help="Student's group.")
    add_parser.add_argument("--gpa", required=True, help="Student's GPA (0-5).")

    list_parser = sub.add_parser("list", help="List all students.")
    list_parser.add_argument("--sort", choices=("fio", "gpa"), help="Sort students by fio or gpa.")
    
    find_parser = sub.add_parser("find", help="Find students by name.")
    find_parser.add_argument("--q", required=True, help="Name substring to search for.")

    remove_parser = sub.add_parser("remove", help="Remove students by name.")
    remove_parser.add_argument("--fio", required=True, help="Student's full name.")

    update_parser = sub.add_parser("update", help="Update a student record.")
    update_parser.add_argument("--fio", required=True, help="Student's full name.")
    update_parser.add_argument("--gpa", help="Student's GPA (0-5).")
    update_parser.add_argument("--group", help="Student's group.")
    update_parser.add_argument("--birthdate", help="Birthdate in YYYY-MM-DD format.")

    stats_parser = sub.add_parser("stats", help = "Show student statistics.")
    stats_parser.add_argument("--n", default=5, help="Number of top students to display.")

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "add":
            student = make_student(
                args.fio,
                args.birthdate, 
                args.group,
                gpa=float(args.gpa)
            )
            add_student(args.db, student)
            print("student added")

        elif args.command == "list":
            students = list_students(args.db, args.sort)
            for student in students:
                print(format_student(student))

        elif args.command == "find":
            found = find_students(args.db, args.q)
            if found:
                for student in found:
                    print(format_student(student))
            else:
                print("student not found")

        elif args.command == "remove":
            count = remove_student(args.db, args.fio)
            print(f"{count} records were removed")

        elif args.command == "update":
            fields = {}

            if args.gpa is not None:
                fields["gpa"] = float(args.gpa)
            if args.group is not None:
                fields["group"] = args.group
            if args.birthdate is not None:
                fields["birthdate"] = args.birthdate

            found = update_student(args.db, args.fio, **fields)

            if found:
                print("record updated")
            else:
                print("student not found")

        elif args.command == "stats":
            result = stats(args.db, args.n)
            pprint(result, sort_dicts=False)
        
    except (ValueError, TypeError, KeyError) as er:
        print(f"Error: {er}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())