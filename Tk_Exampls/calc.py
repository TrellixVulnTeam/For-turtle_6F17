import tkinter as tk


class TNode:
    pass


def newNode(d):
    node = TNode()
    node.data = d
    node.left = None
    node.right = None
    return node


def makeTree(s):
    k = lastOp(s)
    if k < 0:  # создать лист
        Tree = newNode(s)
    else:  # создать узел-операцию
        Tree = newNode(s[k])
        Tree.left = makeTree(s[:k])
        Tree.right = makeTree(s[k + 1:])
    return Tree


def priority(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    if op in '^':
        return 3
    return 100


def lastOp(s):
    minPrt = 50  # любое между 2 и 100
    k = -1
    for i in range(len(s)):
        if priority(s[i]) <= minPrt:
            minPrt = priority(s[i])
            k = i
    return k


def calcTree(Tree):
    if Tree.left == None:
        try:
            return int(Tree.data)
        except:
            return float(Tree.data)
    else:
        if calcTree(Tree.left) == 'Ошибка' or calcTree(Tree.right) == 'Ошибка':
            return 'Ошибка'
        else:
            n1 = calcTree(Tree.left)
            n2 = calcTree(Tree.right)
            if Tree.data == "+":
                res = n1 + n2
            elif Tree.data == "-":
                res = n1 - n2
            elif Tree.data == "*":
                res = n1 * n2
            elif Tree.data == "^":
                res = n1 ** n2
            else:
                try:
                    res = n1 // n2
                except:
                    res = 'Ошибка'
            return res


def calculation(event=0):
    if question.get() != '':
        s = segment(question.get())
        t = makeTree(s)
        answer.insert(1.0, f'{question.get()} = {str(calcTree(t))} \n')
        question.delete(0, 'end')
    else:
        answer.insert(1.0, 'Пустая строка\n')


def segment(s):
   if not valid(s):
        l = len(s)
        c = []
        while s.find(')') != -1:
            for i in range(l-1, -1, -1):
                if s[i] == ')':
                    c.append(i)
                if s[i] == '(':
                    last = c.pop()
                    end = s[last+1:]
                    seg = makeTree(s[i:last+1][1:-1])
                    l = len(s[i:last+1])

                    print('seg = ', s[i:last+1][1:-1])

                    begin = s[:i]
                    middle = str(calcTree(seg))
                    s = begin + str(calcTree(seg)) + end

                    print('s=', s)

                    for g in range(len(c)):
                        c[g] = c[g] - l + len(middle)
        return s
   else:
       return '1/0'


def valid(s):
    L = "("
    R = ")"

    stack = []
    err = False

    for c in s:
        p = L.find(c)
        if p >= 0:
            stack.append(c)
        p = R.find(c)
        if p >= 0:
            if len(stack) == 0:
                err = True
            else:
                top = stack.pop()
                if p != L.find(top):
                    err = True
        if err:
            break

    if len(stack) > 0:
        err = True

    return err


def del_answer():
    answer.delete(0.1, 'end')
    question.delete(0, 'end')


window = tk.Tk()
frame1 = tk.LabelFrame(window, text='Пример')
frame2 = tk.LabelFrame(window, text='Решение')

question = tk.Entry(frame1, width=40, font=('Arial', 20))
calculate = tk.Button(frame1, width=10, text='Вычислить', command=calculation, font=('Arial', 20))

frame1.pack(ipadx=5, ipady=5)
question.pack(pady=5, padx=5)
calculate.pack()

answer = tk.Text(frame2, width=39, height=10, font=('Arial', 20))
scroll_y = tk.Scrollbar(frame2, command=answer.yview, orient='vertical')
answer.config(yscrollcommand=scroll_y.set)

delete = tk.Button(width=10, text='Очистить', command=del_answer, font=('Arial', 20))

frame2.pack()
answer.pack(side='left', pady=5, padx=5)
scroll_y.pack(side='left', fill='y')
delete.pack(pady=5, padx=5)

window.bind('<Return>', calculation)
window.mainloop()
