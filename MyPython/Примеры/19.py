str = input("Введите строку")
print(str)

subStrOld = input("Что меняем: ")
subStrNew = input("На что меняем: ")
lenStrOld = len(subStrOld)

while str.find(subStrOld) > 0:
    i = str.find(subStrOld)
    str = str[:i] + subStrNew + str[i+lenStrOld:]

print(str)
