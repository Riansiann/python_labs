import argparse
from pathlib import Path

from src.lib.text_stats import get_text_stats

def cat_command(input_path: str, numbered: bool = False) -> None:
    path = Path(input_path)

    if not path.is_file():
        raise FileNotFoundError("File not found")

    with path.open("r", encoding="utf-8") as file:
        for number, line in enumerate(file, start = 1):
            if numbered:
                print(f"{number} {line}", end="")
            else:
                print(line, end="")

def stats_command(input_path: str, top: int = 5) -> None:
    path = Path(input_path)

    if not path.is_file():
        raise FileNotFoundError("File not found")

    with path.open("r", encoding="utf-8") as file:
        text = file.read()

    total, unique, top_words = get_text_stats(text, top)

    print(f'Всего слов: {total}')
    print(f'Уникальных слов: {unique}')
    print(f'Топ-{top}:')

    for w, c in top_words:
        print(f'{w}: {c}')


def main():
    parser = argparse.ArgumentParser(
        description="CLI utilities for text processing"
    )
    
    subparsers = parser.add_subparsers(dest = "command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Print file contents")
    cat_parser.add_argument("--input", required=True, help="Path to input file")
    cat_parser.add_argument("-n", action="store_true", help="Print line numbers")

    stats_parser = subparsers.add_parser("stats", help="Show word frequencies")
    stats_parser.add_argument("--input", required=True, help="Path to input text file")
    stats_parser.add_argument("--top", type=int, default=5, help="Number of most frequent words")

    args = parser.parse_args()

    if args.command == "stats" and args.top < 1:
        parser.error('--top must be greater than zero')

    try: 
        if args.command == "cat":
            cat_command(args.input, args.n)
        elif args.command == "stats":
            stats_command(args.input, args.top)

    except FileNotFoundError:
            parser.error(f"File not found: {args.input}")
    except UnicodeDecodeError:
        parser.error(f'File {args.input} cannot be read using UTF-8 encoding')
    


if __name__ == "__main__":
    main()
