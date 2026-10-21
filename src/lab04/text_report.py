from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
import sys

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def main():
    input_path = 'data/lab4/input.txt'
    output_path = 'data/lab4/report.csv'
    try:
        text = read_text(input_path, encoding="utf-8")
    except FileNotFoundError:
        print(f"Файл не найден: {input_path}", file=sys.stderr)
        sys.exit(1)

    normal = normalize(text)
    tokens = tokenize(normal)
    freq = count_freq(tokens)
    rows = sorted_word_counts(freq)
    write_csv(rows, output_path, header = ("word", "count"))

    print(f'Всего слов: {len(tokens)}')
    print(f'уникальных слов: {len(freq)}')
    print('Топ-5:')
    for w, c in top_n(freq, 5):
        print(f'{w}:{c}')

if __name__ == "__main__":
    main()
