from cli import run
import sys

def sum_of_squares(limit):
  sum = 0
  for num in range(1, limit + 1):
    sum += num * num

  return sum

def square_of_sums(limit):
  sum = 0
  for num in range(1, limit + 1):
    sum += num

  return sum * sum

def compute(max):
  return square_of_sums(max) - sum_of_squares(max)

if __name__ == "__main__":
    run(compute, 10)
