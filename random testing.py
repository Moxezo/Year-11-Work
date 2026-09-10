import random
spaces = 1 
count = int(input("How many stairs: "))
print("__")
for step in range(count-1):
    print(f"{spaces*'  '}|_")
    spaces+=1
print(f"{spaces*'__'}|")