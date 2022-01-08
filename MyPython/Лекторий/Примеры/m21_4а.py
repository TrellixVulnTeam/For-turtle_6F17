class decorator(object):

    def __init__(self, f):
        print("внетренний decorator.__init__()")
        f()             # определение функции закончено

    def __call__(self):
        print("внутренний decorator.__call__()")

@decorator

def function():
    print("внутренняя function()")

print("Завершение декорирования function()")

function()
