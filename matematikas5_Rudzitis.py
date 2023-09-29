import math

print('Artūrs, Rudzītis.')
print('\nlaukuma aprēķins ģeometriskām figūrām''\n\t****')

print('Ievadiet malas A garumu:')
MA = float(input()) #Ievada Malu A
print('Malas A garums:',MA,'\n\t****')

print('Ievadiet malas B garumu:')
MB = float(input()) #Ievada Malu B
print('Malas B garums:',MB,'\n\t****')

print('Ievadiet augstumu:')
H = float(input()) #Ievada Augstumu jeb h
print('Augstums:',H,)

Ltri = MA*H/2 #apreiķina Laukumu trijstūrim
print('Laukumu trijstūrim:',Ltri)
Ltra = (MA+MB)/2*H #apreiķina Laukumu trapecei
print('Laukumu trapecei:',Ltra)
Lpar = MA*H #apreiķina Laukumu paralelogramam
print('Laukums paralelogramam',Lpar)

print('\t****','\nPaldies!')