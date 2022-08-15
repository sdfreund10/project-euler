from cli import run
import math

def is_palidrome(num: int):
  if str(num)[::-1] == str(num):
    return True

  return False

def find_product_palidromes(num_digits):
  max_num = int(math.pow(10, num_digits) - 1)
  min_num = int(math.pow(10, num_digits - 1))
  palindromes: list[int] = []

  for x in range(max_num, min_num, -1):
    for y in range(max_num, min_num, -1):
      if x == 91 and y == 99:
        print('should be palidrome here')
      if is_palidrome(x * y):
        palindromes.append(x * y)
        # if only care about largest values, could skip all lower values of y

  return palindromes

def compute(num_digits):
  palindromes = find_product_palidromes(num_digits)
  return max(palindromes)

if __name__ == "__main__":
    run(compute, 2)