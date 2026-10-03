import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    This function normalizes the input text. It performs the following operations:
    1. Converts the text to lowercase.
    2. Replaces the character 'ё' with 'е'.
    3. Replaces tabs and carriage returns with spaces.
    4. Collapses multiple spaces into a single space.
    '''
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е')
    text = text.replace('\t', ' ').replace('\r', ' ')
    text = text.strip()
    text = ' '.join(text.split())
    return text

def tokenize(text: str) -> list[str]:
    '''
    This function tokenizes the input text into a list of words.
    '''
    pattern = r"\w+(?:-\w+)*"
    return re.findall(pattern, text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    '''
    This function counts the frequency of each token in the input list of tokens.
    '''
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''
    This function returns the top n most frequent tokens fron the input frequency dictionary.
    '''
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]



if __name__ == "__main__":
    print("\nRunning tests...")

    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    print("\nNormalize tests passed!")

    # tokenize
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    print("Tokenize tests passed!")

    # count_freq + top_n
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]
    print("Count_freq and top_n tests passed!")

    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    print("Tie-break tests passed!")

    print("\nAll tests passed!")