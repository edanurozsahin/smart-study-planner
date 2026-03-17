dersler = []

while True:
    print("1 - Ders ekle")
    print("2 - Dersleri listele")
    print("3 - Calisma plani olustur")
    print("4 - En cok calisilan dersi goster")
    print("5 - Ders sil")
    print("6 - Cikis")

    secim = input("Seciminiz: ")

    if secim == "1":
        ders_adi = input("Ders adi: ")
        saat = int(input("Gunde kac saat calisilacak? "))

        dersler.append({
            "isim": ders_adi,
            "saat": saat
        })
        print("Ders eklendi.")

    elif secim == "2":
        if len(dersler) == 0:
            print("Henuz ders eklenmedi.")
        else:
            for index, ders in enumerate(dersler, start=1):
                print(f"{index} - {ders['isim']} ({ders['saat']} saat)")

    elif secim == "3":
        if len(dersler) == 0:
            print("Once ders eklemelisin.")
        else:
            gunler = [
                "Pazartesi",
                "Sali",
                "Carsamba",
                "Persembe",
                "Cuma",
                "Cumartesi",
                "Pazar"
            ]

            plan = []

            for ders in dersler:
                for i in range(ders["saat"]):
                    plan.append(ders["isim"])

            print("Haftalik plan:")

            for gun, ders in zip(gunler, plan):
                print(f"{gun} -> {ders}")

    elif secim == "4":
        if len(dersler) == 0:
            print("Henuz ders eklenmemis.")
        else:
            en_fazla = max(dersler, key=lambda x: x["saat"])
            print("En cok calisilan ders:")
            print(f"{en_fazla['isim']} ({en_fazla['saat']} saat)")

    elif secim == "5":
        if len(dersler) == 0:
            print("Silinecek ders yok.")
        else:
            for index, ders in enumerate(dersler, start=1):
                print(f"{index} - {ders['isim']}")

            sil = int(input("Silmek istedigin ders numarasi: "))

            if 1 <= sil <= len(dersler):
                silinen = dersler.pop(sil - 1)
                print(f"{silinen['isim']} silindi.")
            else:
                print("Gecersiz numara.")

    elif secim == "6":
        print("Program kapatildi.")
        break

    else:
        print("Hatali secim yaptiniz!!!")