import solutions.p6 as p6

def test_p6():
  example = p6.compute(10)
  assert example == 2640
  answer = p6.compute(100)
  print('Problem 6 solution:', answer)
  assert answer == 25164150
