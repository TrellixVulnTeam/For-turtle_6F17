class Reverse:
    """Итератор для переворачивания последовательности"""
    def __init__(self, data):       # инициализация 
        self.data = data            # переменной задается значение параметра
        self.index = len(data)      # определяем длину параметра
    def __iter__(self):             # включаем итерационный процесс
        return self
    def __next__(self):
        if self.index == 0:         # если длина == 0
            raise StopIteration     # вызов исключения, останавливающего итерацию
        self.index = self.index - 1 # если не равна, то индекс уменшаем на единицу
        return self.data[self.index]# и возвращаем предыдущий элемент
    
rev = Reverse('spam')
for char in rev:
        print(char)                 # каждый вывод дает следующий (с конца) элемент
