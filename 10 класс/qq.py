def key_sort(x):
    sum = 0
    while x > 0 :
        sum = sum + x % 10
        x = x // 10
    return sum
    

print(key_sort(12321))