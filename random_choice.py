#choice
import random
carbrands=["acura","bmw","porshe","ferrari"]
print(random.choice(carbrands))
print(" ")
#sample
fruits=["guava","apple","orange","tangarines","kiwi"]
print(random.sample(fruits,k=3))
print(" ")
myvar=range(20)
print(random.sample(myvar,k=7))
print(" ")
myvar_1=range(2,15)
print(random.sample(myvar_1,k=6))
print(" ")
myvar_2=range(4,15,3)
print(random.sample(myvar_2,k=3))
print(" ")
"""myset={"apple","samsung","nokia","redmi","tecno"}
print(random.sample(myset,k=3))"""



