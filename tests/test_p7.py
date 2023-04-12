import p7

def test_p7():
  example = p7.compute(6)
  assert example == 13
  answer = p7.compute(10_001)
  print('Problem 7 solution:', answer)
  assert answer == 104743
