from cli import run
from util import get_product

def is_pythagorean_triplet(a, b, c):
  return a * a + b * b == c * c

def find_triplets_for_triangle(perimeter_length: int):
  triplets: list[list[int]] = []
  max_length = int(perimeter_length / 2)
  for a in range(1, max_length):
    for b in range(1, a):
      c = perimeter_length - a - b
      if is_pythagorean_triplet(a, b, c):
        triplets.append([a, b, c])

  return triplets

def compute(perimeter_length):
  triplets = find_triplets_for_triangle(perimeter_length)

  if len(triplets) == 0:
    print('No triplets found')
    return None
  elif len(triplets) > 1:
    print('More than one triplet found. Returning largest product')
    return max([get_product(trip) for trip in triplets])
  else:
    return get_product(triplets[0])
    

if __name__ == "__main__":
    run(compute, 12)