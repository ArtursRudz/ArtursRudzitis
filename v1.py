#izdrukt skaitļus 0,1,2,3,4,5
for i in range (6): #defaultā sāksies ar 0
    print(i)
print('--------------------------')
#izdrukāt 3,5,7
for i in range (3,8,2):
    print(i)

n = int(input("Ievadīt skaitli:"))
for i in range(1,11):
    print(n,'+',i,'=',n+i)
print('--------------------------')
#atrast skaitļu 2 un 4 dalītājus
#uz ekrāna parādīt tos, kas dalās ar 2, tos, kas dalās garn ar 4, gan 2
#range 50
#num = int(input('Ievadi veselu range skaitli: '))
#for i in range(2,num+1,2):
#    print (i,'Dalās tikai ar 2')               <---- Meiģinājums
#for i in range(4,num+1,4):
#   print (i,'Dalās gan ar 2 gan ar 4')
num_range = int(input("Ievadiet cik skaitļus drukāsiet"))
for i in range(num_range):
    if i % 2 == 0 and i % 4 == 0:
        print(i, "Dalās ar 2 un 4")
    elif i % 2 == 0 and i % 4 != 0:
        print(i, "Dalās tikai ar 2")
