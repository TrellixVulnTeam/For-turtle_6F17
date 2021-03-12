mul1, mul2 = map(int, input().split())

mul = 0

for i in range(abs(mul1)):
    mul += abs(mul2)


print(-mul if ((mul1 > 0) and (mul2 < 0)) or
      ((mul1 < 0) and (mul2 > 0)) else mul)
