pasazieruSk = int(input('Cik pasažieru brauks taksī?: '))
Pfunkcija = input('Vai jums patīk kaķi? (j/n): ')

if pasazieruSk > 4 or Pfunkcija == 'j':
    print('Nevar izsaukt taksi')
elif pasazieruSk <= 4:
    plkst = int(input('Ievadiet pulksteņa laiku, jāievada veseļos skaitļos.(no 1 līdz 24): '))
    if plkst < 1 or plkst > 24:
        print('Ievadiet pareizus datus.')
        exit()
    if plkst < 23 and plkst > 5:
        plkstM = 0.47
    elif plkst > 1 or plkst < 24:
        Noligsana = input('Vai taksis ir stāvietā pie dzelsceļa stacijas? (j/n): ')
        plkstM = 0.87
        NoligsanaM = 2.40
        if Noligsana != 'j' and Noligsana != 'n':
            print('Ievadiet pareizus datus.')
            exit()
        if Noligsana == 'j':
            NoligsanaM = 1.20
        elif Noligsana == 'j' or Noligsana == 'n':
            gaidisanaL = int(input('Ievadiet gaidīšanas laiku minūtēs: '))
            gaidisanaM = gaidisanaL * 0.15
            Cels = int(input('Cik tālu būs taksim jābraudz km?: '))
            CelsM = Cels * plkstM
            print(f'Sākuma maksa = {NoligsanaM} \nGaidīšanas maksa = {gaidisanaM} \nCeļa maksa = {CelsM}')
            
            