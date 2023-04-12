import p4

def test_p4():
  example = p4.compute(2)
  assert example == 9009
  answer = p4.compute(3)
  print('Problem 4 solution:', answer)
  assert answer == 906609
