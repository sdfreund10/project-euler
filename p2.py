from cli import run

def generate_fib(max: int):
  nums = [1, 2]
  while nums[-1] + nums[-2] < max:
    nums.append(nums[-1] + nums[-2])

  return(nums)

def select_even(nums: list[int]):
  return([x for x in nums if x % 2 == 0])

def compute(max):
  sequence = generate_fib(max)
  return sum(select_even(sequence))


if __name__ == "__main__":
    run(compute, 10)