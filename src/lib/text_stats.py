from src.lib.text import (
    normalize,
    tokenize,
    count_freq,
    top_n
)

def get_text_stats(text: str, top: int = 5) -> tuple:
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, top)

    return len(tokens), len(freq), top_words
