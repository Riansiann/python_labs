import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Data converters")
    sub = parser.add_subparsers(dest="command", required=True)

    json_parser = sub.add_parser("json2csv", help="Convert a JSON file to CSV format.")
    json_parser.add_argument("--in", dest="input", required=True, help="Path to the input JSON file.")
    json_parser.add_argument("--out", dest="output", required=True, help="Path to the output CSV file.")

    csv_parser = sub.add_parser("csv2json", help="Convert a CSV file to JSON format.")
    csv_parser.add_argument("--in", dest="input", required=True, help="Path to the input CSV file.")
    csv_parser.add_argument("--out", dest="output", required=True, help="Path to the output JSON file.")

    xlsx_parser = sub.add_parser("csv2xlsx", help="Convert a CSV file to XLSX format.")
    xlsx_parser.add_argument("--in", dest="input", required=True, help="Path to the input CSV file.")
    xlsx_parser.add_argument("--out", dest="output", required=True, help="Path to the output Excel XLSX file.")

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

    