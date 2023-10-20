'''atbilde = 'j'
while atbilde == 'j':
    print('Nekusties!')
    atbilde = input('Vai briesmonis ir draudzīgs?(j/n): ')
print('Bēdz prom!')'''

#pārbaudīt vai lietotājs prot reizināt ar 7
#Programma atkārto darbību līdz brīdim, kad uzdoti visi 12 jautājumi
reiz = int(input('Reizinātājs:'))  #reizinātāju ievada lietotājs
for i in range(1,13): #cikla mainīgais no 1-12
    print("Cik ir",i,"x",reiz,'?')
    minejums = input()
    if minejums == 'stop':
        print('Programma beidzas.')
        break #pātrauc programmu
    if minejums == 'izlaist':
        print('Lābi, izlaižam.')
        continue #izlaiž 1 jautājumu un turpina tālāk
    atb = i * reiz
    if atb == int(minejums):
        print('Pareizi')
    else:
        print('Nē, tas ir nepareizi, pareizi ir:',atb)
        #ja ir neparezi, tad atgriežas pie jautājuma