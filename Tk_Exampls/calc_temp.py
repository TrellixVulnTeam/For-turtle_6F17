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


def segment(s):
    n_s = ''
    while len(s) > 0:
        temp = s[0]
        s = s[1:]
        if temp == '(':
            aux, s = segment(s)
            n_s = n_s + aux
        elif temp == ')':
            print(n_s)
            tree = makeTree(n_s)
            res = calcTree(tree)
            return str(res), s
        else:
            n_s += temp
    return n_s





s = '1--2'
s = s.replace('--', '+')
print(s)
print(s.replace('--', '+'))
