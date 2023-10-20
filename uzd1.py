#for cikls
'''for i in range(10):
    print(str(i)*i)
print()'''

''''gadi = int(input('Ievadi suņu gadus?:'))
if gadi <= 0:
    exit()
elif gadi <= 2:
    gadiCilveku = gadi * 10.5
    gadi = gadi - 2
    if gadi >= 3:
       gadiCilveku = gadiCilveku + gadi * 4
    else:
        print('Suņu gadi Cilvēku gados ir:',gadiCilveku)'''


#for i in range(1,21):
#    print(i,'.autobusa pietura')

for i in range(1,8):
    print('*'*i)
for star in range(6,0,-1):
    print('*'*star)

rinda = 7
for i in range(0,rinda):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
for i in range(rinda, 0, -1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")