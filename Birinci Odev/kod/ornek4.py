liste = [1,3,8,9,7,5,1,2]

for i in liste :
    sayac = 1
    if i*2 in liste :
        sayac = sayac+1
    else:
        pass
    print(i,"için aynı sayı",sayac,"kez mevcut")
