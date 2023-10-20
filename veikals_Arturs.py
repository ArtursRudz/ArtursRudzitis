vaiVissNopirkts = 'n'
kurIepirksies = int(input('Ievadiet cik procentu atlaide ir balstoties uz to kur iepirksities.\nRimi atlaide ir 30%\nElvi ir 40% atlaide ja ir karte\nMaxima ir 20% atlaide un ja ir karte tad 50% atlaide\nTop ir 30% ja pērk 3 preces un vairāk\nIevadiet procentus šadi (40):'))
procenti= kurIepirksies / 100 
ciklssk = 0
listSk=0
precuDaudz= []
preces= []
cenas = []
while vaiVissNopirkts == 'n':
    prece = input('Ievadi preci: ')
    preces.append(prece)
    if prece.isnumeric():
        print('Nepareizi dati')
        exit()
    precesDaudz = input('Ievadiet preču daudzumu: ')
    precuDaudz.append(precesDaudz)
    if int(precesDaudz) <=0:
        print('Nepareizi dati')
        exit()
    cena = float(input('Ievadi preces cenu(piem:1.20): '))
    cena =(cena - float(procenti))*float(precesDaudz)
    cenas.append(cena)
    if cena <=0.0:
        print('Nepareizi dati')
        exit()
    vaiVissNopirkts = input('Vai ir nopirkts viss, kas sarakstā?(j/n): ')
    ciklssk = ciklssk + 1
for i in range(0,ciklssk,1):
    print(f'{preces[listSk]}\tDaudzums:{precuDaudz[listSk]}\t{round(cenas[listSk],1)} eiro')
    listSk = listSk + 1
print(f'kopā: {round(sum(cenas),1)}')