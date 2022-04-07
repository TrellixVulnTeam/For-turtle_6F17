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
            res = n1 // n2
        return res


def calculation():
    s = question.get()
    t = makeTree(s)
    question.delete(0, 'end')
    answer.insert(1.0, f'{s} = {str(calcTree(t))} \n')


def del_answer():
    answer.delete(0.1, 'end')


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
delete.pack()

window.mainloop()
