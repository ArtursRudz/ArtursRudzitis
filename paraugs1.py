telefons = {
    'Jānis':28313735,
    'Anna':28329456,
    'Ivars':32018586
}
#Jānim ir 2 telefona numuri
telefons.update({'Jānis':22222245})
print('Šis ir Annas telefons:',telefons['Anna'])
print('Šis ir Jāņa telefons:',telefons['Jānis'])
print('Šis ir Ivara telefons:',telefons['Ivars'])

#Izveidot vārdnīcu ar atslēhu virkni un fromkeys() metodi
#vārdnīca nenorādot ierakstu vērtības
kk = ('viens','divi','trīs')
dd = dict.fromkeys(kk)
print(dd)
vert = 0 #šī vērtība būs visai vārdnīcai
dd = dict.fromkeys(kk,vert)
print(dd)

#izveidot vārdnīcu, kas satur sarakstu

valstis = {
    'Vācija':['Berlīna','frankfurta','Hamburga'],
    'Nīderlande':['Amsterdama','Tillsburga','Rotterdama'],
    'Lietuva':['Vilnius','Siauliai','Panavaži']
}

for atslega, vertiba in valstis.items():
    for i in vertiba:
        print("{}: {}".format(atslega,i))