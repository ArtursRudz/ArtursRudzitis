sk1 = int(input('Ievadi skaitli 1: '))
sk2 = int(input('Ievadi skaitli 2: '))

# Noteikumus grupē iekavās pārlasāmībai.
# Katras iekavas pārbauda vai skaitlis ir mazāks par 50 un lielāks par 15, un pēc tam abas iekavas salīdzina.
if (sk1 > 15 and sk1 < 50) and (sk2 > 15 and sk2 < 50):
    print('Tu saņēmi 1 punktu par šo uzdevumu!')
elif (sk1 > 15 and sk1 < 50) or (sk2 > 15 and sk2 < 50): 
    print('Pārlasi noteikumus!')
else:
    print('Uzdevums nav izpildīts!')
    
