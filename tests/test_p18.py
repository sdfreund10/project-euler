import p18

def test_p18():
  example = p18.compute(4)
  assert example == 23
  answer = p18.compute(15)
  print('Problem 18 solution:', answer)
  assert answer == 1074
