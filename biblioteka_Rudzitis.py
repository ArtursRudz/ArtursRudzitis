persProf = str(input('Vai jūs esat students?: ')) #Uzzinam vai ir students vai personāls
persPastIzd = str(input('Vai tu esi šobrīd nenodevuši grāmatu laikā?: ')) #uzzinam vai ir nenodevis kādu grāmatu laikā
ZorB = str(input('Vai jūs pasūtat grāmatu?: ')) #Uzzinam vai pasūta grāmatu vai žurnālu
BpieprIzd = str(input('Vai šīs ir prieprasītos izdevumos?: ')) #Vai ir pieprasītos izdevumos

if persPastIzd == 'jā': #ja ir nenodevis grāmatu tad neizdod
    print('Nevar izdot, jo nav atdota grāmata vau žurnāls.')
elif BpieprIzd == 'jā': #ja ir pieprasīta tad 2 dienas
    print('Raksts tiek izdots uz 2 dienām.')
elif ZorB == 'nē': #ja ir žurnāls
    print('Žurnalu izdod uz 7 dienām.')
elif persProf == 'jā':# ja ir students un zinam ka ir grāmata tad izdod uz 14 dienām
     print('Grāmatu tiek izdota uz 14 dienām.')
elif persProf == 'nē': # ja ir personāls tad izdod uz 28 dienām
    print('Grāmatu tiek izdota uz 28 dienām.')
else:
    print('Kaut ko nepareizi ievadijāt.')