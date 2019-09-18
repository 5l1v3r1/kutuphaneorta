import os
kitapliste = list()



menu ="""

Mr.Felix Kütüphane Otomasyon Uygulaması (Orta Seviye)



[1]-Kitap Ekle
[2]-Kitap Al
[3]-Tüm Kitapları Listele
[4]-Çıkış Yap

"""

def kitapekle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Ekleme İşlemi Tamamlandı.")
    print("Ana Menüye Dönmek Lütfen Enter'a Basınız.")
    input()


def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kitapcikar(kitap:tuple,liste:list):

    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Kitap Çıkartma Tamamlandı.")
        print("Ana Menüye Dönmek İçin  Lütfen Enter'a Basınız.")
        input()

    else:
        print("Aradığınız Kitap Malesef Sistemde Mevcut Değildir.")
        print ("Ana Menüye Dönmek İçin Enter'a Basınız.")
        input ()

def listele(liste:list):
    for i in liste:
        print("Kitap Adı : {}     <>>>>>>>>   Kitap Yazarı : {}       ".format(i[0],i[1]))

    print("Ana Menüye Dönmek Enter'a Basınız.")
    input()


while True:

    os.system("clear")
    print(menu)


    secim = input("İşleminizi Seçiniz   :")

    if  secim == "1":
        kitapadi =input("Kitap Adı Giriniz  :")
        kitapyazar=input("Kitap Yazar Adı Giriniz  :")
        kitap=(kitapadi,kitapyazar)
        kitapekle(kitap,kitapliste)#Kitap Ekleniyor.


    elif secim =="2":
        kitapadi = input ("Kitap Adı Giriniz  :")
        kitapyazar = input ("Kitap Yazar Adı Giriniz  :")
        kitap = (kitapadi, kitapyazar)
        kitapcikar(kitap,kitapliste)

    elif  secim =="3":
        listele (kitapliste)

    elif secim =="4":
        print("Keyifli Okumalar Diler Yine Yeniden Bekleriz.")
        quit()

    else:
        print("Malesef Hatalı Giriş Yaptınız  :")




