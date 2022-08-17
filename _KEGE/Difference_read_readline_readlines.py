import linecache

f = open("4429.txt") #read (всё сразу)
lines = f.read()
print(type(lines))
print(lines)
f.close()

f = open("4429.txt") #readline (по строчно)
line = f.readline()
print(type(line))
print(line)
while line:
    print(line)
    line = f.readline()
f.close()

f = open("4429.txt") #readlines (всё сразу в список)
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

text = linecache.getline("4429.txt", 2)  # Выходная строка 2
print(text)
