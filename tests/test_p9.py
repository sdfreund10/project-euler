import solutions.p9 as p9

def test_p9():
  example = p9.compute(12)
  assert example == 3 * 4 * 5
  answer = p9.compute(1000)
  print('Problem 9 solution:', answer)
  assert answer == 31875000
