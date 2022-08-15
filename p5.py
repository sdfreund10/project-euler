from cli import run
import math

from p3 import prime_factors

def factor_counts(num):
  factors = prime_factors(num)
  counts: dict[int, int] = {}
  for factor in factors:
    counts[factor] = counts.get(factor, 0) + 1
  return counts

def find_common_factors(nums):
  factor_subset: dict[int, int] = {}

  for num in nums:
    factors = factor_counts(num)

    for factor, count in factors.items():
      if factor_subset.get(factor, 0) < count:
        factor_subset[factor] = count

  return factor_subset

def smallest_common_divisor(sequence_end):
  nums = list(range(1, sequence_end + 1))

  factors = find_common_factors(nums)

  num = 1
  for factor, count in factors.items():
    num = num * math.pow(factor, count)

  return int(num)

def compute(sequence_end):
  return smallest_common_divisor(sequence_end)

if __name__ == "__main__":
    run(compute, 10)