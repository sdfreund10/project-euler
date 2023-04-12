import p15

def test_p15():
  example = p15.compute(2)
  assert example == 6
  answer = p15.compute(20)
  print('Problem 15 solution:', answer)
  assert answer == 137846528820
