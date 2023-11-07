saraksts = [7,1,9,4,6,4,3,6]
saraksts.append('Cepums') #pievieno beigās
print(saraksts)

saraksts.pop()#izmet no beigām
print(saraksts)

saraksts.insert(3,'Hello!') #ievieto 3. vietā 
print(saraksts)

saraksts.remove('Hello!') #izdzēš norādīto vērtību
print(saraksts)

#funkcijas del pielietojums
tests = [1,2,3,4,5,6,7,8]
del tests[2] #izdēš vienu elementu
print(tests)

del tests[3:6]
print(tests) #izdzēš intervālu

cipari = [1,2,3,4,5,6,7,8]
del cipari[2:7:2] #no 2-7 elementam dzēš ārā katru otro
print(cipari)