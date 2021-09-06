f = open('merfi.txt','r')
line = f.readline()
print(line, end='')
i = 2
while len(line)>0:
    line = f.readline()
    print(line,end='')
    i+=1
    if i % 15 == 0:
        a = input()     # просто остановка вывода через каждые 15 строк
                        # для продолжения работы программы нужно нажать <Enter>
f.close()
