import random
#akmns,skeres,papirs
gajieni = ['akmens','papirs','skeres']#saraksts
while True:
    cilveka_gajiens = input('Ievadi savu gajienu:')
    datora_gajiens = random.choice(gajieni)
    print('Cilveks:',cilveka_gajiens,'vs Dators:',datora_gajiens)
    if cilveka_gajiens == datora_gajiens:
        print('Neizskirts!')
    elif cilveka_gajiens == 'akmens' and datora_gajiens == 'skeres':
        print('Cilveks uzvar!')
    elif cilveka_gajiens == 'skeres' and datora_gajiens == 'papirs':
        print('Cilveks uzvar!')
    elif cilveka_gajiens == 'papirs' and datora_gajiens == 'akmens':
        print('Cilveks uzvar!')
    else:
        print('Dators uzvar!')