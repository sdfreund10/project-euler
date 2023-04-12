from solutions.cli import run
import math

def primes_below_num(num: int):
  if num <= 2:
    return []

  primes = [2]

  def is_prime(x: int):
    for prime in primes:
      if x % prime == 0:
        return False
      if prime > math.sqrt(x):
        return True
    return True

  for i in range(3, num):
    if is_prime(i):
      primes.append(i)
  
  return primes

def compute(limit):
  primes = primes_below_num(limit)
  return sum(primes)

if __name__ == "__main__":
    run(compute, 10)