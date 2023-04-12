import solutions.p5 as p5

def test_p5():
  example = p5.compute(10)
  assert example == 2520
  answer = p5.compute(20)
  print('Problem 5 solution:', answer)
  assert answer == 232792560
