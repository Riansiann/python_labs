from pathlib import Path 
from typing import Iterable, Sequence
import csv

def read_text(path: str | Path, encoding = "utf-8") -> str:
    '''
    Reads text file and returns its contents as a single string.
    UTF-8 encoding is used by default. 
    A different encoding can be specified: read_text("name_of_a_file.txt, encoding="cp1251").
    Raises:
        FileNotFoundError: if the file does not exist.
        UnicodeDecodeError if the file cannot be decoded with the specified encoding.
    '''
    p = Path(path)
    return p.read_text(encoding=encoding)

def ensure_parent_dir(path: str | Path) -> None:
    '''
    Creates parent directories for the specified path
    if they do not already exist.
    '''
    p = Path(path)
    p.parent.mkdir(parents = True, exist_ok = True)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    Writes data to a CSV file using UTF-8 encoding.
    Checks that all rows have the same length.
    Raises ValueError if row lengths do not match.
    """
    p = Path(path)
    rows = list(rows)

    if rows:
        row_len = len(rows[0])
        for row in rows:
                if len(row) != row_len:
                    raise ValueError("All rows must have same length")
        if header is not None:
            if len(header) != row_len:
                raise ValueError("Header and rows must have same length")
        
    ensure_parent_dir(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
