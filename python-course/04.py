#DICTIONARIES

#key-value pair

monster1={"name":"guru","power":10,"color":"red"}

print(monster1["name"]) #guru

#key ekleme
monster1["position"]=100
print(monster1);

#erişim
print(monster1.get("position"))
print(monster1.get("boy"))

#update
monster1.update({"name":"GURU","power":20})

#del 
del monster1["power"]

#pop kullanımı da same

#key values

print(monster1.values())
print(monster1.keys())
print(monster1.items())

for key in monster1:
    print(key) #name color position

#
friends=[{"name":"bengisu","surname":"şahin"},{"name":"cansu","surname":"şahin"}]
print(friends[0]["name"]) #bengisu
