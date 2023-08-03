#VARIABLES

#Strings
name="bengisu"

#F strings
msg=f"merhaba {name}"
print(msg)
#length
print(len(msg))
#index
print(name[0]) 
#slicing
print(name[0:6]) #0. karakter dahil 6. dahil değil === print(name[:6]) 

#title
print(name.title()) 

#upper -lower
print(name.upper()) 
print(name.lower()) 

#count --> verilen karakterin dizide kaç tane olduğunu gösterir
print(name.count("b")) #1

#find-> karakter kaçıncı sırada
print(name.find("b"))

#replace
print(name.replace("bengisu","cansu"))

#help - değişken icin kullanabileceğim metotları gösterir
print(dir(name)) 
print(help(str))


#NUMBERS

x=17
y=11.1
z="5"

#Bölme
print(5/3)  #1.6666667

#Tam Bölme
print(5//3) #1

#Üs Alma
print(5**3) #125

#Mutlak Değer
num=-5
print(abs(num)) #5

#Round
m=6.78
print(round(num)) #7
print(round(num,1)) #6.8

#Pow
print(pow(4,2)) #16

#Min-Max
print(max(4,3,6,11)) #11

#String + 
num1="24"
num2="41"
print(num1+num2) #2441

#String to Int
num1=int(num1)
num1=int(num1)
print(num1+num2) #65

#String mult
str="test"
print(str*4) # test test test test