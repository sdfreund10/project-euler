import p11

def test_p11():
  example = p11.compute(1)
  assert example == 99
  answer = p11.compute(4)
  print('Problem 11 solution:', answer)
  assert answer == 70600674
