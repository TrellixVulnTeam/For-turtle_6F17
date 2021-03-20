def if1(int_number):
    if(int_number >0 ):
        return(int_number-8)
    else:
        return(int_number)
    return int_number


def if2(int_number):
    if(int_number >0 ):
        return(int_number-8)
    else:
        return(int_number+6)


def if3(int_number):
    if(int_number>0 ):
        return(int_number-8)
    elif int_number==0:
        return(10)
    else:
        return(int_number+6)


def if4(int1,int2,int3):
    if int1>0 and int2>0 and int3>0:
        return(3)
    elif int1>0 and int2>0 and int3<=0:
        return(2)
    elif int1>0 and int2<=0 and int3>0:
        return(2)
    elif int1<=0 and int2>0 and int3>0:
        return(2)
    elif int1<=0 and int2<=0 and int3<=0:
        return(0)
    else:
        return(1)    


def if5(int1,int2,int3):
    a = False
    b = False
    if int1>0 and int2>0 and int3>0:
        a =3
    elif int1>0 and int2>0 and int3<0:
        a = 2
        b = 1
    elif int1>0 and int2<0 and int3>0:
        a = 2
        b = 1
    elif int1<0 and int2>0 and int3>0:
        a = 2
        b = 1
    elif int1<0 and int2<0 and int3<0:
        b = 3
    elif int1==0 and int2==0 and int3>0:
        b = 0
        a = 1
    elif int1==0 and int2>0 and int3==0:
        b = 0
        a = 1
    elif int1>0 and int2==0 and int3==0:
        b = 0
        a = 1
    elif int1==0 and int2==0 and int3<0:
        b = 1
        a = 0
    elif int1==0 and int2<0 and int3==0:
        b = 1
        a = 0
    elif int1<0 and int2==0 and int3==0:
        b = 1
        a = 0
    elif int1==0 and int2==0 and int3==0:
        a = 0
        b = 0
    elif int1>0 and int2==0 and int3<0:
        b = 1
        a = 1
    elif int1<0 and int2>0 and int3==0:
        b = 1
        a = 1
    elif int1==0 and int2<0 and int3>0:
        b = 1
        a = 1
    else:
        a = 1
        b = 2
    return a, b


def if6(int1,int2):
    if(int1>int2):
        return(int1)
    elif int1==int2:
        return int1
    else:
        return(int2)   


def if7(int1,int2):
    if(int1>int2):
        return(int2)
    elif int1==int2:
        return int1
    else:
        return(int1)  





def if8(int1,int2):
    if(int1>int2 ):
        return(int1,int2)
    elif int1==int2:
        return int1
    else:
        return(int2,int1)
    



def if9(a,b):
    a, b = (min(a, b), max(a, b))
    return(a, b)


def if10(a,b):
    if a==b :
        a=0
        b=0
        return(a, b)
    elif a>b:
        a=b+a
        b=a
        return(a, b)
    else:
        a=b+a
        b=a
        return(a, b)
    



def if11(a,b):
    if a==b :
        a=0
        b=0
        return(a, b)
    elif a>b:
        b=a
        return(a, b)
    else:
        a=b
        return(a, b)
    



def if12(int1,int2,int3):
    if (int1<=int2) and (int1<=int3):
        return(int1)
    elif (int2<=int1) and (int2<=int3):
        return(int2)
    else:
        return(int3)
    



def if13(float1, float2, float3):
    """
    If13. Даны три числа. Найти среднее из них (т.е. число, расположенное между наименьшим и наибольшим).
    """
def if13(float1, float2, float3):
    if ((float2<=float1) and (float1<=float3))or((float2>=float1) and (float1>=float3)):
        return(float1)
    elif ((float1<=float2) and (float2<=float3))or((float1>=float2) and (float2>=float3)):
        return(float2)
    else:
        return(float3)
    

def if14(float1, float2, float3):
    """
    If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.
    """
def if14(float1, float2, float3):
   n= min(float3,min(float1,float2))
   m=max(float3,max(float1,float2))
   return(n,m)   



def if15(float1, float2, float3):
    """
    If15. Даны три числа. Найти сумму двух наибольших из них.
    """
def if15(float1, float2, float3):
   n= min(float3,min(float1,float2))
   return(float1+float2+float3-n)

