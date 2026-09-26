def get_info(fio):
    parts = fio.split()
    initials = f'{parts[0][0]}{parts[1][0]}{parts[2][0]}.'.upper()
    length = len(" ".join(parts))

    return initials, length

fio = input("ФИО: ")
initials, length = get_info(fio)
print(f'Инициалы: {initials}\nДлина (символов): {length}')


