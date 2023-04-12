from solutions.cli import run

def sum_of_digits(num: int):
  return sum([
    int(digit) for digit in str(num)
  ])


def compute(power: int):
  # clear cache from last run
  return sum_of_digits(2 ** power)

if __name__ == "__main__":
    run(compute, 15)