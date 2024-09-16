"""Hocam kullanıcıdan alınan sayı değerne kadar toplayan bir uygulama yapmak istedim biraz daha güzel olsun :)"""
print("Hoşgeldiniz!")
sayiSinir = int(input("Lütfen 0'dan hangi sayıya kadar toplamak istiyorsanız girin : "))
s = sayiSinir
sayac = sayiSinir+1
topla = 0
while sayac>0 :
    topla = topla + (sayiSinir)
    sayac = sayac-1
    sayiSinir = sayiSinir-1

print(s,"'dan/den sıfıra kadar olan sayıların toplamı : ",topla)

"""Bu da sadece 100'den geri :)"""
print("Hoşgeldiniz!")
sayi = 100
s = 100
sayac = sayi+1
topla = 0
while sayac>0 :
    topla = topla + (sayi)
    sayac = sayac-1
    sayi = sayi-1

print(s,"'den sıfıra kadar olan sayıların toplamı : ",topla)
