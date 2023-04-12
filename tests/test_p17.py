import solutions.p17 as p17

def test_p17():
  example = p17.compute(5)
  assert example == 19
  assert p17.length_of_words(342) == 23
  assert p17.length_of_words(115) == 20
  answer = p17.compute(1000)
  print('Problem 17 solution:', answer)
  assert answer == 21124
