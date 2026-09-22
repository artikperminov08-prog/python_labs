fam, name, otch = [i for i in list(input("Фио: ").split())]
leng = len(fam) + len(name) + len(otch) + 2
print(f'Инициалы: {fam[0].upper()}{name[0].upper()}{otch[0].upper()}')
print(f'Длина (символов): {leng}')
