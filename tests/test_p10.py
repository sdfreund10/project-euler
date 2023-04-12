import p10

def test_p10():
  example = p10.compute(10)
  assert example == 17
  answer = p10.compute(2_000_000)
  print('Problem 10 solution:', answer)
  assert answer == 142913828922
