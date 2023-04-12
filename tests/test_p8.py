import solutions.p8 as p8

def test_p8():
  example = p8.compute(4)
  assert example == 5832
  answer = p8.compute(13)
  print('Problem 8 solution:', answer)
  assert answer == 23514624000
