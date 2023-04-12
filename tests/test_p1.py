import p1

def test_p1():
  example = p1.compute(10)
  assert example == 23
  answer = p1.compute(1000)
  print('Problem 1 solution:', answer)
  assert answer == 233168
