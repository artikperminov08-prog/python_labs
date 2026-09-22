fam, name, otch = [i for i in list(input("Фио: ").split())]
leng = len(fam) + len(name) + len(otch) + 2
print(f'Инициалы: {fam[0]}{name[0]}{otch[0]}')
print(f'Длина (символов): {leng}')