#FUNCTIONS

def func(name,age=23):
    print(f'Hello {name}, you are {age} is old ')

func("bengisu")
func("cansu",33)

#pass
def func1():
    pass
func1()

#LAMBDA
#İstediğimiz kadar argüman kullanabiliriz ancak tek bir işlem yaptırabiliriz

y=lambda a:a**2
print(y(5))

addFive=lambda x:x+5
print(addFive(10))

mult = lambda m,n : m * n
print(mult(10,8))