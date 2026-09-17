minutes = int(input('Минуты: '))
hhr = minutes // 60
mmr = minutes % 60
print(f'{hhr}:{mmr:02d}')