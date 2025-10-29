a=""
class Lisanslar:
    def zeropd():
        print("\n")
        print("CC0 Sıfır (Zero): Kamu Malı tahsisi olarak kullanılır. Kullanımda olan son sürümü 1.0’dır. Resmi olarak Türkçe çevirisi yayınlanmıştır. Bu lisans kapsamında telif hakkı sınırlaması yoktur, kaynak atıf vermeden ticari amaç da dahil olmak üzere kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
        Lisanslar.a="CC0"
    def ccby():
        print("\n")
        print("CC BY Atıf (Attribution): En esnek CC lisansıdır. Kaynak atıf verilmesi koşuluyla, kopyalanabilir, dağıtılabilir, düzenlenebilir ve ticari amaçlarla kullanılabilir.") 
        Lisanslar.a="CC BY"
    def ccbysa():
        print("\n")
        print("CC BY-SA Atıf - Paylaşım Aynı Lisansla (Attribution-ShareAlike): Kaynak atıf verilmesi koşuluyla, kopyalanabilir, dağıtılabilir, düzenlenebilir ve ticari amaçlarla kullanılabilir. Eserden türetilen yeni eserler de aynı lisansla paylaşılmalıdır.")
        Lisanslar.a="CC BY-SA"
    def ccbync():
        print("\n")
        print("CC BY-NC Atıf - Ticari Olmayan (Attribution-NonCommercial): Kaynak atıf verilmesi koşuluyla, kopyalanabilir, dağıtılabilir ve düzenlenebilir ancak ticari amaçlarla kullanılamaz.")  
        Lisanslar.a="CC BY-NC"
    def ccbyncsa():
        print("\n")
        print("CC BY-NC-SA Atıf - Ticari Olmayan - Paylaşım Aynı Lisansla (Attribution-NonCommercial-ShareAlike): Kaynak atıf verilmesi koşuluyla, kopyalanabilir, dağıtılabilir ve düzenlenebilir ancak ticari amaçlarla kullanılamaz. Eserden türetilen yeni eserler de aynı lisansla paylaşılmalıdır.")
        Lisanslar.a="CC BY-NC-SA"
    def ccbyncnd():
        print("\n")
        print("CC BY-NC-ND Atıf - Ticari Olmayan - Türetilemez (Attribution-NonCommercial-NoDerivatives): Kaynak atıf verilmesi koşuluyla, kopyalanabilir ve dağıtılabilir ancak ticari amaçlarla kullanılamaz ve eser üzerinde değişiklik yapılamaz.")
        Lisanslar.a="CC BY-NC-ND"
    def ccbynd():
        print("\n")
        print("CC BY-ND Atıf - Türetilemez (Attribution-NoDerivatives): Kaynak atıf verilmesi koşuluyla, kopyalanabilir ve dağıtılabilir ancak eser üzerinde değişiklik yapılamaz.")
        Lisanslar.a="CC BY-ND"

    def mesaj():
        return "Bu bir lisans uygulama modülüdür. Lisans türlerini kullanabilirsiniz."
    def turler():
        print("Lisans Türleri:")
        print("1. CC0 Sıfır (Zero)")
        print("2. CC BY Atıf (Attribution)")
        print("3. CC BY-SA Atıf - Paylaşım Aynı Lisansla (Attribution-ShareAlike)")
        print("4. CC BY-NC Atıf - Ticari Olmayan (Attribution-NonCommercial)")
        print("5. CC BY-NC-SA Atıf - Ticari Olmayan - Paylaşım Aynı Lisansla (Attribution-NonCommercial-ShareAlike)")
        print("6. CC BY-NC-ND Atıf - Ticari Olmayan - Türetilemez (Attribution-NonCommercial-NoDerivatives)")
        print("7. CC BY-ND Atıf - Türetilemez (Attribution-NoDerivatives)")
    
    def veri():
        calismaismi= input("Çalışma ismini girin: ")
        kimyapti= input("Çalışmayı yapan kişinin ismini girin: ")
        clink= input("Çalışma linkini girin: ")
        yprofil= input("Yapan kişinin profil linkini girin: ")
        yil= input("Yılı girin: ") 

        print("\n")
        print( calismaismi +" © "+yil+" by "+kimyapti+" is licensed under "+Lisanslar.a +" License.\nLink: "+clink+"\nProfile: "+yprofil)