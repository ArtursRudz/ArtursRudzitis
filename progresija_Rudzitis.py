print('Aritmētiskas progresijas elementu apreķins \nIevadiet pirmo locekli!')
pirmaisLoceklis = int(input())
print('Ievadiet diferenci!')
diference = int(input())
print('Ievadiet elementu sakitu!')
elementuSkaits = int(input())
LoceklisSk = 1

for i in range(pirmaisLoceklis,elementuSkaits * diference + pirmaisLoceklis,diference):
    print (f'{LoceklisSk}. loceklis:\t{i}')
    LoceklisSk = LoceklisSk + 1 
