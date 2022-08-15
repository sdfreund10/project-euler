import math

from cli import run

def find_next_prime(primes):
  max_prime = 2
  if len(primes) > 0:
    max_prime = max(primes)

  for num in range(max_prime + 1, max_prime * 2):
    is_prime = True

    for prime in primes:
      if num % prime == 0:
        is_prime = False
        break

    if is_prime:
      return num

  return max_prime * 2

# Mostly the same, but with some early-exits to reduce iterations
def find_next_prime_fast(primes):
  # ensure the primes are sorted
  #   This increases the initial overhead, but allows for some quick-exits later
  primes.sort()
  max_prime = 2
  if len(primes) > 0:
    max_prime = primes[-1]

  for num in range(max_prime + 1, max_prime * 2):
    is_prime = True
    sqrt =  math.sqrt(num)

    for prime in primes:
      # The largest factor of any number is the sqrt
      #   since the primes are sorted, all the subsequent primes
      #   are bigger than the sqrt and thus can't be factors
      if prime > sqrt:
        break

      if num % prime == 0:
        is_prime = False
        break

    if is_prime:
      return num

  return max_prime * 2


def generate_primes(num):
  primes = [2]

  while len(primes) < num:
    primes.append(find_next_prime_fast(primes)) 

  return primes

def compute(n):
  primes = generate_primes(n)
  return primes[-1]

if __name__ == "__main__":
    run(compute, 6)
