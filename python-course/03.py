#TUPLES

#Oluşturduğumuz veri grubunun içeriğinin değimemesini istediğimiz durumlarda kullanırız.

capitals=("tahran","ankara","madrid","tiflis")
print(len(capitals)) #4
print(capitals[0]) #tahran
print(capitals[1:3]) #ankara , madrid

#capitals[0]="paris" -> hata döndürür çünkü tuples nesnesi değiştirilemez.

capitals=("berlin","londra") #tuple mızı yeniden tanımlaya biliriz

#del capitals -> silme işlemi

#SET
#Set elemanları unique dir. Bir elemandan sadece 1 adet vardır.
cities={"izmir","ankara","istanbul","eskişehir"}
#print(cities[0]) --> hata 

#Eleman ekleme
cities.add("bursa")

cities.update(["edirne","aydın"])
print(cities)

#Eleman kaldırma
cities.remove("bursa")
cities.discard("istanbul")
cities.discard("istanbulabc") #bunu remove da yapsaydık hata alırdık

cities.clear()
