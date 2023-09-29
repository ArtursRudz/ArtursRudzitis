sk1 = int(input('Ievadi skaitli 1: '))
sk2 = int(input('Ievadi skaitli 2: '))

print(f'Ievadītie skaitļi: {sk1}, {sk2}')

if sk1 * sk2 > 0: # Ja skaitlis lielāks par 0, tas ir pozitīvs.
    print(f'Skaitļu reizinājums pozitīvs, summa: {sk1 + sk2}')
elif sk1 * sk2 < 0: # Ja mazāks par 0 - negatīvs.
    print('Skaitļu reizinājums negatīvs, ievadiet citus skaitļus')
    sk1, sk2 = int(input('Ievadi skaitli 1: ')), int(input('Ievadi skaitli 2: '))
else: # Skaitļu reizinājums ir 0 / viens no skaitļiem ir 0
    print('Skaitļu reizinājums ir 0.')