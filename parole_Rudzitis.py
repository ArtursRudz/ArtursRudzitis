Lietotajvards = 'akmens' 
Parole = '123456'
meiginajumi = 4 #Cik meiģinājumi ir atlikuši
summa = 0
for i in range (1,6,1):
    Lietotajvards_ievadits = input('Ievadi savu lietotājvārdu:') #Iegūstu ievdītos datus
    if Lietotajvards_ievadits == 'stop':
        print('Programma beidzas!')
        exit()
    Parole_ievadits = input('Ievadi savu paroli: ')
    if Parole_ievadits == 'stop':
        print('Programma beidzas!')
        exit()
    elif Parole_ievadits != Parole and len(Parole_ievadits) != len(Parole):#pārbauda vai parole ir pareiza un vai paroles raktszīmju skaits ir vienāds ar pareizo paroli
        if meiginajumi == 0: #ja meiginājumi visi pieci ir imantoti programma beidzas
            print('Atļauts mēģināt pieslēgties 5 reizes!')
            exit()
        print(f'Parole ir jābūt {len(Parole)} raktzīmes garai!\nIr atlikuši {meiginajumi} meiģinājumi')#Parāda cik raktszīmes grai ir jābūt un cik vēl meiģinājumi
        meiginajumi -= 1 #Viens meiginājums ir imantots
    elif Lietotajvards_ievadits != Lietotajvards or Parole_ievadits != Parole: #Pārbauda vai lietotājvārds un parole
        if meiginajumi == 0 : #ja meiginājumi visi pieci ir imantoti programma beidzas
           print('Atļauts mēģināt pieslēgties 5 reizes!')
           exit()
        print(f'Ir atlikuši {meiginajumi} meiģinājumi')
        meiginajumi -= 1
    elif Lietotajvards_ievadits == Lietotajvards and Parole_ievadits == Parole: 
        print('Peislēgšanas veiksmīga')
        break
primaisVeselaisSk = input('Ievadiet 1. veselo sakitli: ')#Lietotājs ievada pirmo veselo skaitli
if primaisVeselaisSk == 'stop':#Pārbauda vai lietotājs saka stop ja jā tad programma beidzās
    print('Programma beidzas!')
    exit()
otraisVeselaisSk = input('Ievadiet 2. veselo sakitli: ')
if otraisVeselaisSk == 'stop':
    print('Programma beidzas!')
    exit()
elif int(otraisVeselaisSk) <= -1 or int(primaisVeselaisSk) <= -1:#Pārbauda vai skaitļi ir negatīvi
    print('Nedrīkst būt negatīvs skaitlis')
    exit()
elif int(otraisVeselaisSk) <= int(primaisVeselaisSk):#Pārbauda vai pirmais skaitlis ir lielāks par otro skaitli
    print('Nevar 1. veselais skaitlis būt lielāks par 2. veselo skaitli')
    exit()
for i in range (int(primaisVeselaisSk),int(otraisVeselaisSk)+1,1):#Veidojot virkni katru skaitli pieskaita summai
    summa += i
print (f'Veselu secīgi pieaugošu sakitļu no {primaisVeselaisSk} līdz {otraisVeselaisSk} summa ir {summa}.') 



        
        