user = "Андрей"
action = "покупка"
 
log_message = 'Пользователь {} зашел на сайт и выполнил действие: {}'.format(
    user,
    action
)
 
print(log_message)

user = "Юрий"
action = "продажа"
 
log_message = f'Пользователь {user} зашел на сайт и выполнил действие: {action}'
 
print(log_message)

def sentence_has_animal(sentence: str) -> bool:
    return "animal" in sentence
 
print(sentence_has_animal("У Ивана есть своя собственная Bitcoin ферма"))


import time
 
def fib(number: int) -> int:
    if number == 0: return 0
    if number == 1: return 1
    
    return fib(number-1) + fib(number-2)
 
start = time.time()
fib(40)
 
print(f'Duration: {time.time() - start}s')
