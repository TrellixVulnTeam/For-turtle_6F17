def ten_numbers_min_max(n): # Замечательные числа 2
    min_number = n[0]
    max_number = n[0]
    for i in n:
        if min_number > i:
            min_number = i
        if max_number < i:
            max_number = i
   
    print(f'максимальных - {n.count(max_number)}, минимальных - {n.count(min_number)}')

n = (1,2,5,3,5,9,5,32,1,32,6,-4,5,-4,5,4,32,21,0)
ten_numbers_min_max(n)