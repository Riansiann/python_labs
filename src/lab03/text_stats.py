from src.lib.text import normalize, tokenize, count_freq, top_n
import sys

table_flag = 1
raw_text = sys.stdin.read()
if raw_text.strip() == "":
    raise ValueError("Input text is empty.")

normalized_text = normalize(raw_text)
tokens = tokenize(normalized_text)
unique_tokens = set(tokens)
freq = count_freq(tokens)
top_tokens = top_n(freq, n=5)

print('Всего слов:', len(tokens))
print('Уникальных слов:', len(unique_tokens))
print('Топ-5 слов:')

if not table_flag:
    for token, count in top_tokens:
        print(f'{token}: {count}')

else:
    max_token_length = max(len(token) for token, _ in top_tokens)
    print(f'{'слово':<{max_token_length}} | {'частота'}')
    print('-' * (max_token_length + 12))
    for token, count in top_tokens:
        print(f'{token:<{max_token_length}} | {count}')


