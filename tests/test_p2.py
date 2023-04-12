import solutions.p2 as p2

def test_p2():
  example = p2.compute(100)
  assert example == 2 + 8 + 34
  answer = p2.compute(4_000_000)
  print('Problem 2 solution:', answer)
  assert answer == 4613732
