import time


def isPrime ( n ):
  k = 2
  while k*k <= n and n % k != 0:
    k += 1
  return (k*k > n)

t0 = time.time()

print(isPrime(100000000000))

t1 = time.time() - t0
print("Time elapsed: ", t1)
