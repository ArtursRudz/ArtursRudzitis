import math
import random

print('Ievadiet riņka līnijas rādiusu:')
RLr = float(input()) #Ievada riņka līnijas rādiusu
print(RLr)
RLg = 2*math.pi*RLr #apreiķina riņka līnijas garumu
RLl = math.pi*math.pow(RLr,2) #apreiķina riņka līnijas laukumu
print('Riņķa līnijas garums:',"%.2f"%RLg)
print('Riņķa līnijas laukums:',"%.2f"%RLl)

print('Ievadiet taisnleņķa trijstūra pirmās katetes garumu:')
K1 = float(input())  #Ievada pirmo kateti
print('Ievadiet taisnleņķa trijstūra otrās katetes garumu:')
K2 = float(input())  #Ievada otro kateti
Hip = math.sqrt(math.pow(K1,2)+math.pow(K2,2)) #apreiķina hipotenūzu imantojot pitagoras teorēmu
print('Taisnleņķa trijstūra hipotenūzas garums:',"%.2f"%Hip)

print('Gadījuma sakitlis no 0 - 1:', random.random())