import math
import random
skaitlis = 43.7
print('Noapalots uz leju:',math.floor(skaitlis))
print('Noapalots uz augsu:',math.ceil(skaitlis))

print('Mainiga pakāpe',math.pow(skaitlis,2))
print(math.pow(4,6))#pirmais skaitlis ir tas ko kāpina, un otrais ir kapinātājs
pakape = 3
print(math.pow(skaitlis,pakape))
print('Kvadrātsakne:',math.sqrt(skaitlis))

x = 256971/2641
print('x:',x)
print('Formatēts x: ' "%.3f"%x)
print('Formatēts x: ' "{:.2f}".format(x))

cipars = random.random() #0.1 - 1.0
print(cipars)

cipars2 = random.randint(1,50)
print(cipars2)