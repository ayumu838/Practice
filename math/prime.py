import math
import time
num = 1000000000
def is_prime(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    else:
        for i in range(3,int(math.sqrt(num))):
            if num % i == 0:
                return False
    return True


def main():
    primes = []
    for i in range(num):
        if is_prime(i):
            primes.append(i)

start_time = time.time()
main()
elapsed_time = time.time() - start_time
print(elapsed_time)
