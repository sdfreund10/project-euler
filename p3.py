from cli import run

def prime_factors(num: int):
  factors = []
  upper_limit = int(num / 2)
  for divisor in range(2, upper_limit + 1):
    if num == 1:
      break
    while num % divisor == 0:
      factors.append(divisor)
      # guaranteed to be an integer if we get here, but need to cast
      # for the sake of consistent type signitures
      num = int(num / divisor)

  if len(factors) == 0:
    return [num]

  return factors


def compute(num):
  factors = prime_factors(num)
  return factors[-1]

if __name__ == "__main__":
    run(compute, 13195)