def segment(s):
    l = len(s)
    c = []
    while s.find('(') != -1:
        for i in range(l-1, -1, -1):
            if s[i] == ')':
                c.append(i)
            if s[i] == '(':
                last = c.pop()
                end = s[last+1:]
                seg = s[i:last+1]
                begin = s[:i]
                print(begin, seg, end)
                s = begin + 'N' + end
                print('s=',s)

s = '(Для уроков (составитель тестов)+(2+3))-(4+5)'
print(segment(s))
