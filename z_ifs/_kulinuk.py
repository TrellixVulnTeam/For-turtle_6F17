def if1(int_number):
    if int_number>0:
        int_number=int_number-8
        return(int_number)
    else:
        return(int_number)



def if2(int_number):
    if int_number>0:
        int_number=int_number-8
        return(int_number)
    else:
        int_number=int_number+6
        return(int_number)


def if3(int_number):
    if int_number>0:
        int_number=int_number-8
        return( int_number)
    elif int_number == 0:
        int_number=10
        return(int_number)   
    else:
        int_number=int_number+6
        return(int_number)

def if4(int1, int2, int3):
    n=0
    if int1*-1<0:
        n=n+1         
    if int2*-1<0:
        n=n+1         
    if int3*-1<0:
        n=n+1
    return(n)


def if5(int1, int2, int3):
    n=0
    n1=0
    if int1*-1>0:
        n=n+1
    elif int1==0:
        n=n
        n1=n1
    else:
        n1=n1+1
    if int2*-1>0:
        n=n+1
    elif int2==0:
        n=n
        n1=n1
    else:
        n1=n1+1        
    if int3*-1>0:
        n=n+1
    elif int3==0:
        n=n
        n1=n1
    else:
        n1=n1+1
    return(n1, n)


def if6(int1, int2):
    if int1>int2:
        return(int1)
    elif int2>int1:
        return(int2)
    elif int1==int2:
        return(int2)


def if7(int1, int2):
    if int1>int2:
        return(2)
    elif int2>int1:
        return(1)
    elif int1==int2:
        return(2)


def if8(int1, int2):
    if int1>int2:
        return(int1,int2)
    elif int2>int1:
        return(int2,int1)
    elif int1==int2:
        return(int2,int1)


def if9(a, b):
    if a>b:
        a,b=a,b
        return(a,b)
    elif a==b:
        return(a,b)
    else:
        return(a,b)


def if10(a, b):
    if a!=b:
        a,b=a+b,a+b
        return(a,b)
    elif a==b:
        a,b=0,0
        return(a,b)


def if11(a, b):
    if a>b:
        a,b=a,a
        return(a,b)
    elif b>a:
        a,b=b,b
        return(a,b)
    elif a==b:
        a,b=0,0
        return(a,b)


def if12(int1, int2,int3):
    if int1<int2 and int1<int3:
        return(int1)
    elif int2<int1 and int2<int3:
        return(int2)
    elif int3<int1 and int3<int2:
        return(int3)
    elif int3==int1 and int3<int2:
        return(int3)
    elif int2==int1 and int2<int3:
        return(int2)
    elif int2==int3 and int3<int1:
        return(int3)
    elif int1==int2==int3:
        return(int1)


def if13(float1,float2,float3):
    if float1>float2 and float1<float3:
        return(float1)
    elif float2>float1 and float2<float3:
        return(float2)
    elif float3>float1 and float3<float2:
        return(float3)
    elif float3>float2 and float3<float1:
        return(float3)
    elif float1>float3 and float1<float2:
        return(float1)
    elif float2>float3 and float2<float1:
        return(float2)
    elif float1==float2==float3:
        return(float3)


def if14(float1, float2, float3):
    a=0
    b=0
    if float1<float2 and float1<float3:
        a=float1
    elif float1>float2 and float1>float3:
        b=float1
               
    if float2<float1 and float2<float3:
        a=float2
    elif float2>float1 and float2>float3:
        b=float2
    elif float2==float1 and float3<float3:
        a=float3
        b=float1                    
    if float3<float1 and float3<float2:
        a=float3
    elif float3>float1 and float3>float2:
        b=float3
    elif float3==float2 and float3<float1:
        a=float3
        b=float1
    elif float3==float1 and float3<float2:
        a=float3
        b=float2
    return(a,b)
        

def if15(float1, float2, float3):
    a=0
    if float2>float1 and float3>float1:
        a=float2+float3
    elif float1>float2 and float3>float2:
        a=float1+float3
    elif float2>float3 and float1>float3:
        a=float1+float2
    elif float2>float3 and float1>float3:
        a=float1+float2
    elif float1==float2 and float1>float3:
        a=float1+float2
    elif float1==float3 and float1>float2:
        a=float1+float3
    elif float2==float3 and float2>float1:
        a=float2+float3
    elif float1==float2 and float1<float3:
        a=float3+float2
    elif float1==float3 and float1<float2:
        a=float2+float3
    elif float2==float3 and float2<float1:
        a=float1+float3
    return(a)
    