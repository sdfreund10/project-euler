import solutions.p3 as p3

def test_p3():
  example = p3.compute(13195)
  assert example == 29
  answer = p3.compute(600851475143)
  print('Problem 3 solution:', answer)
  assert answer == 6857
