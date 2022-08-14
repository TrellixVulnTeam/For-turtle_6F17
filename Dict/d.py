files = open('dictionary-Для уроков (составитель тестов).lib', 'r', encoding="utf-8")
files_refactoring = open('dictionary_refactoring.lib', 'w', encoding="utf-8")
temp = '\n'
for lines in files:
    aux = ''
    k = 0
    while 'A' <= lines[k] <= 'z' or lines[k] in (' ', '/', '-', '.', ','):
        aux += lines[k]
        k += 1
    aux += '*** ' + lines[k:]


    print(aux)
    if not lines==temp=='\n':
        files_refactoring.write(aux)
    else:
        temp = lines

files.close()
files_refactoring.close()
