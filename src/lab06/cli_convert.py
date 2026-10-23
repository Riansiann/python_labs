import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command", required=True)

    json_parser = sub.add_parser("json2csv")
    json_parser.add_argument("--in", dest="input", required=True)
    json_parser.add_argument("--out", dest="output", required=True)

    csv_parser = sub.add_parser("csv2json")
    csv_parser.add_argument("--in", dest="input", required=True)
    csv_parser.add_argument("--out", dest="output", required=True)

    xlsx_parser = sub.add_parser("csv2xlsx")
    xlsx_parser.add_argument("--in", dest="input", required=True)
    xlsx_parser.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        parser.error(f"File not found: {args.input}")
    except ValueError as error:
        parser.error(str(error))

if __name__ == "__main__":
    main()

    