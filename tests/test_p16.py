import solutions.p16 as p16

def test_p16():
  example = p16.compute(15)
  assert example == 26
  answer = p16.compute(1000)
  print('Problem 16 solution:', answer)
  assert answer == 1366
