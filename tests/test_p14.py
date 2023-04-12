import solutions.p14 as p14

def test_p14():
  example = p14.generate_collatz_sequence(13)
  assert example == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
  answer = p14.compute(1000000)
  print('Problem 14 solution:', answer)
  assert answer == (837799, 525)
