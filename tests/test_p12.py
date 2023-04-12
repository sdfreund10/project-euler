import solutions.p12 as p12

def test_p12():
  example = p12.compute(5)
  assert example == 28
  answer = p12.compute(500)
  print('Problem 12 solution:', answer)
  assert answer == 76576500
