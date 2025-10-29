import uygulama
print(uygulama.Lisanslar.mesaj())
print(uygulama.Lisanslar.turler())

while True:
    try:
        secim = int(input("Lisans türü numarasını girin (1-7): "))
        if secim == 1:
            uygulama.Lisanslar.zeropd()
            break
        elif secim == 2:
            uygulama.Lisanslar.ccby()
            break
        elif secim == 3:
            uygulama.Lisanslar.ccbysa()
            break
        elif secim == 4:
            uygulama.Lisanslar.ccbync()
            break
        elif secim == 5:
            uygulama.Lisanslar.ccbyncsa()
            break
        elif secim == 6:
            uygulama.Lisanslar.ccbyncnd()
            break
        elif secim == 7:
            uygulama.Lisanslar.ccbynd()
            break
        else:
            print("Geçersiz seçim.") 
            break
    except ValueError: 
        print("Lütfen geçerli bir numara girin.")

sozluk={1:"CC0",2:"CC BY",3:"CC BY-SA",4:"CC BY-NC",5:"CC BY-NC-SA",6:"CC BY-NC-ND",7:"CC BY-ND"}
calismaismi= input("Çalışma ismini girin: ")
kimyapti= input("Çalışmayı yapan kişinin ismini girin: ")
clink= input("Çalışma linkini girin: ")
yprofil= input("Yapan kişinin profil linkini girin: ")
yil= input("Yılı girin: ") 

print("\n")
print( calismaismi +" © "+yil+" by "+kimyapti+" is licensed under "+sozluk[secim]+" License.")
    