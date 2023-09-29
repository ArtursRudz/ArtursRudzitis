skaitlis1 = int(input('Ievadi skaitli 1:'))
skaitlis2 = int(input('Ievadi skaitli 2:'))

# Skaitļu izvade ar fstring
print(f'Pirmais skaitlis {skaitlis1}\nOtrais skaitlis: {skaitlis2}')

# Ja pirmais skaitlis ir vienāds ar 3, pieskaita tam 3, bet ja nav - abus skaitļus atņem iekšpus fstring formatēšanas.
if skaitlis1 == 3:
    print(f'Pirmais skaitlis ir 3, otrajam pieskaitot 3 rezultāts ir: {skaitlis2 + 3}')
else:
    print(f'Pirmais skaitlis nav 3, atņemot otro skaitli no pirmā rezultāts ir: {skaitlis1 - skaitlis2}')
    