sk1 = int(input('Ievadi skaitli 1: '))
sk2 = int(input('Ievadi skaitli 2: '))

# Skaitļu salīdzināšana
if sk1 > sk2:
    print(f'Pirmais skaitlis lielāks nekā otrs, starpība: {sk1 - sk2}')
elif sk1 < sk2:
    print(f'Pirmais skaitlis mazāks nekā otrs, summa {sk1 + sk2}')
else: # Neviens no skaitļiem nav lielāks par otru
    print('Skaitļi ir vienādi.')