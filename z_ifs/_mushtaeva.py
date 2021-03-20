def if1(int_number):
    if int_number>0:
        f=int_number-8
        return(f)
    else:
        return(int_number)

def if2(int_number):
    f = False
    if int_number>0:
        f=int_number-8
    elif int_number<0:
        f=int_number+6
    return(f)

def if3(int_number):
    if int_number==0:
        return(10)
    elif int_number>0:
        f=int_number-8
        return(f)
    else:
        f1=int_number+6
        return(f1) 
        

def if4(int1,int2,int3):
    if int1>0:
        int1==1
    elif int2>0:
        int2==1
    elif int3>0:
        int3==1
    else:
        return(0)


def if5(int1, int2, int3):
    k=d=0
    
    if int1>0:
        d==d+1
    if int1<0:
        k==k+1
   
    if int2>0:
        d==1+d 
    if int2<0:
        k==1+k
      
    if int3>0:
        d==1+d  
    if int3<0:
        k==1+k
    return(d, k)

def if6(int1, int2):
    if int1>int2:
        return('Больше ',int1)
    else:
        return('Больше ',int2)


def if7(int1, int2):
    if int1>int2:
        return('1')
    else:
        return('2')


def if8(int1, int2):
    if int1>int2:
        return(int1,int2)
    else:
        return(int2,int1)

def if9(a, b):
    if (a>b):
        a=a+b
        b=a-b
        a=a-b
        return(a,b)
    else:
        return(a,b)


def if10(a, b):
    if a!=b:
        a=b+a
        b=b+a
    elif a==b:
        a=b=0
    return(a,b) 

def if11(a, b):
    if a!=b and a<b:
        a=b
    elif a!=b and  a>b:
        b=a
    elif a==0 and b==0:
        a=b=0

    return(a,b)


def if12(int1, int2, int3):
    if (int1<=int2) and (int1<=int3):
        return(int1)
    elif (int2<=int3) and (int2<=int3):
        return(int2)
    else:
        return(int3)


def if13(float1, float2, float3):
    if (float2<=float1) and (float1<=float3) or(float2>=float1) and (float1>=float3):
        return(float1)
    elif (float1<=float2) and (float2<=float3) or(float1>=float2) and (float2>=float3):
        return(float2)
    else:
        return(float3)

def if14(float1, float2, float3):
    if (float1<=float2) and (float1<=float3):
        x =float1
    elif (float2<=float2) and (float2<=float3):
        x = float2
    else:
        x = float3
    if (float1>=float2) and (float1>=float3):
        x = float1
    elif (float2>=float2) and (float2>=float3):
        x = float2
    else:
        x = float3
    return x


def if15(float1, float2, float3):
    if (float1>=float2) and (float1>=float3):
        if float2>=float3:
            return(float1+float2)
        else:
            return(float1+float3)
    elif (float2>=float1) and (float2>=float3):
        if float1>=float3:
            return(float1+float2)
        else:
            return(float2+float3)
    else:
        if float1>=float2:
            return(float1+float3)
        else:
            return(float2+float3)
