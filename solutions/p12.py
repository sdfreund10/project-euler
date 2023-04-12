from solutions.cli import run
import math

def get_factors(num):
  factors = [1,num]
  for i in range(1, int(math.sqrt(num))):
    if num % i == 0:
      factors.append(i)
      factors.append(num / i)
  return list(set(factors))

def find_highly_divisable_triangle_num(num_divisors: int):
  triangle_number_index = 1
  current_triangle_number = 1

  max_num_factors_found = 0
  max_num = current_triangle_number

  found_target = False

  while not found_target:
    unique_factors = get_factors(current_triangle_number)

    if len(unique_factors) >= num_divisors:
      found_target = True
    else:
      triangle_number_index += 1
      current_triangle_number += triangle_number_index

  return current_triangle_number

compute = find_highly_divisable_triangle_num

if __name__ == "__main__":
    run(compute, 5)