def list_2(): # Количество совпадающих пар
    c=0
    a=[int(input()) for i in range(int(input()))]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                c+=1
    print(c)
list_2()