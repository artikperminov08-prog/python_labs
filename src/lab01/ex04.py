m = int(input("Минуты: "))
hours = m//60
mins = m - hours*60
print(f'{hours}:{mins:02d}')