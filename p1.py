from cli import run

def collect_multiples(max: int):
  nums: list[int] = []
  for num in range(1, max):
    if (num % 3 == 0 or num % 5 == 0):
      nums.append(num)
  return nums

def sum_multiples(max: int):
  multiples = collect_multiples(max)
  return(sum(multiples))

def compute(n):
  return sum_multiples(n)

if __name__ == "__main__":
    run(sum_multiples, 10)
