import p13

def test_p13():
  example = p13.compute(2)
  assert example == 55
  answer = p13.compute(10)
  print('Problem 13 solution:', answer)
  assert answer == 5537376230
