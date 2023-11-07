'''>Izveidot 3 sarakstus: lietotājs pats norādīs cik elementus likt sarakstā.
>Pirmā un otrā saraksta vērtības ievada lietotājs.
>Treša saraksta vērtības iegūst apvienojot pirmos 2 sarakstus.
>Katra saraksta saturu glīti parādīt uz ekrāna.'''

lietotaja_1_saraksts = []
lietotaja_2_saraksts = []
kopejais_saraksts = []

cikls_sk1 = int(input('Cik liels būs 1. saraksts: '))
for i in range(cikls_sk1):
    pagaidas_vertiba= input('Ieraksti 1. saraksta elementu: ')
    lietotaja_1_saraksts.append(pagaidas_vertiba)
    
cikls_sk2 = int(input('Cik liels būs 2. saraksts: '))
for j in range(cikls_sk2):
    pagaidas_vertiba= input('Ieraksti 2. saraksta elementu: ')
    lietotaja_2_saraksts.append(pagaidas_vertiba)

kopejais_saraksts = lietotaja_1_saraksts + lietotaja_2_saraksts
'''print('1.saraksta elementi:')
for elements in lietotaja_1_saraksts:
    print(elements)
print('2.saraksta elementi:')
for elements in lietotaja_2_saraksts:
    print(elements)
print('kopējā saraksta elementi:')
for elements in kopejais_saraksts:
    print(elements)'''
print(lietotaja_1_saraksts)
print(lietotaja_2_saraksts)
print(kopejais_saraksts)

saraksts1 =[]
saraksts2= []
#pirmais saraksts
print('Ievadi saraksta garumu: ')
garums = int(input()) #lietotājs pats ievada saraksta lielumu

for i in range(garums):
    lieta1 = input('Ievadiet saraksta elementu: ')
    saraksts1.append(lieta1)
print("Pirmā sarakata elementi:",saraksts1)

print('Ievadi saraksta garumu: ')
garums2 = int(input()) #lietotājs pats ievada saraksta lielumu
for j in range(garums2):
    lieta2 = input('Ievadiet saraksta elementu: ')
    saraksts2.append(lieta2)
print("Pirmā sarakata elementi:",saraksts2)

jauns_saraksts = [saraksts1+saraksts2]
print(jauns_saraksts)
