from solutions.cli import run

def collatz_mutate(num: int):
  if num == 1:
    return num
  if num % 2 == 0:
    return int(num / 2)
  
  return 3 * num + 1

# Original solution
def generate_collatz_sequence(starting_num: int):
  sequence = [starting_num]

  while sequence[-1] != 1:
    sequence.append(collatz_mutate(sequence[-1]))

  return sequence
    

def find_longest_collatz_sequence(limit: int):
  longest = 1
  length = 0
  for i in range(1, limit):
    sequence = generate_collatz_sequence(i)
    if len(sequence) > length:
      longest = i
      length = len(sequence)

  return longest, length

# Optimized solution, caching sequence lengths and shortcutting computation
#   once it encounters a number it has seen before
collatz_sequence_length_cache: dict[int, int] = {}
def collatz_sequence_length(starting_num: int):
  sequence_length = 1
  current_value = starting_num

  while current_value != 1:
    if current_value in collatz_sequence_length_cache:
      sequence_length += collatz_sequence_length_cache[current_value] - 1
      current_value = 1
    else:
      sequence_length += 1
      current_value = collatz_mutate(current_value)

  collatz_sequence_length_cache[starting_num] = sequence_length
  return sequence_length

def find_longest_collatz_sequence_fast(limit: int):
  longest = 1
  length = 0
  for i in range(1, limit):
    sequence_length = collatz_sequence_length(i)
    if sequence_length > length:
      length = sequence_length
      longest = i

  return longest, length
    

def compute(limit):
  return find_longest_collatz_sequence_fast(limit)

if __name__ == "__main__":
    run(compute, 10)