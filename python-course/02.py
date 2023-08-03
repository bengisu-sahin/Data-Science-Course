#LİSTE YAPISI
#Değişik veri tiplerinden oluşan veri topluluklarıdır.

cities=["Prag","Madrid","İzmir","Eskişehir","Floransa"]
print(cities) #["Prag","Madrid","İzmir","Eskişehir","Floransa"]
print(cities[0]) #Prag
print(len(cities)) #5
print(cities[-1]) #Floransa
print(cities[-2]) #Eskişehir

#Slicing
print(cities[0:2]) #["Prag","Madrid","İzmir"]
print(cities[:-1]) #["Prag","Madrid","İzmir","Eskişehir"]

cities[0]="İstanbul"
print(cities[0]) #İstanbul

#Append
cities.append("Ankara") #sonuna ekler

#Insert
cities.insert(0,"Belgrad") #kacıncı indekse ekleyeceğini belirt

#Delete
del cities[0] #0. indeksteki elemanı siler

#Pop
cities.pop() #sondaki elemanı siler

#Remove
cities.remove("İzmir")

#Sort kalıcı olarak sıralar
cities.sort() #alfabetik sıralar
cities.sort(reverse=True) #alfabetik tersi sıralar

#Sorted o an için sıralar 
print(sorted(cities))

#index öğrenme
print(cities.index("Madrid")) #dont use
print("Madrid" in cities) #true

#FOR ile liste elemanları üzerinde gezinme
for city in cities:
    print(city)

for city in cities:
    print(f'City Name: {city}')

#String to List
myStr="tokyo,madrid,kiev"
myList=myStr.split(",")
print(myList)

#Range
for num in range(1,5):
    print(num) #1 2 3 4

for num in range(2,11,2):
    print(num) #2 4 6 8 10

#Range ile list oluşturma
nums=list(range(1,11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#For döngüsü ile list oluşturma
myNums=[num for num in range(1,11)]

#Referans 
c1=["ali","veli","can"]
c2=c1 #aynı memory belleğini gösteren 2 pointer gibi düşün

c3=c1[:] #bu sefer farklı yeri point eden farklı bir list oluşturulmuş oldu