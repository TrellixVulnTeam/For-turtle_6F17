# Что делает данная программа:

n = int(input("Задайте число: "))
length = 0

while n > 0:
    n //= 10
    length += 1
    
print("Получили: ",length)

