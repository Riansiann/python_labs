fio = input("ФИО: ")
parts = fio.split()
initials = f'{parts[0][0]}{parts[1][0]}{parts[2][0]}.'.upper()
length = len(" ".join(parts))
print(f'Инициалы: {initials}\nДлина (символов): {length}')

