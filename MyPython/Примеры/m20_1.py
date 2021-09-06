class Stack:
    def __init__(self):
       """Инициализация стека"""
       self._stack = []
    def top(self):
       """Возвратить вершину стека (не снимая)"""
       return self._stack[-1]
    def pop(self):
       """Снять со стека элемент"""
       return self._stack.pop()
    def push(self, x):
       """Поместить элемент на стек"""
       self._stack.append(x)
    def __len__(self):
       """Количество элементов в стеке"""
       return len(self._stack)
    def __str__(self):
       """Представление в виде строки"""
       return " : ".join(["%s" % e for e in self._stack])
s = Stack()
s.push(1)
s.push(2)
s.push("abc")
print (s.pop())
print (len(s))
print (s)

